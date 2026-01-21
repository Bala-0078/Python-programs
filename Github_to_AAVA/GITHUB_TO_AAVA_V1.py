import os
import requests
from dotenv import load_dotenv
import json
import base64
import uuid

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
accessKey=os.getenv("access_key")
REPO_NAME = "Bala-0078/dictionary_site"
BRANCH = "main"
BASE_URL = "https://api.github.com"

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Accept": "application/vnd.github+json"
}
headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "access-key": accessKey,
    }

url="https://avaplus-internal.avateam.io/force/platform/pipeline/api/v1/execute"

def get_repo_contents(path):
    url = f"{BASE_URL}/repos/{REPO_NAME}/contents/{path}"
    params = {"ref": BRANCH}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

def grouping_fileContents_in_dict(
    start_path="backend",
    package_name=None
):
    java_files = {}
    if package_name:
        path = f"{start_path}/{package_name}"
    else:
        path=start_path
    contents = get_repo_contents(path)

    while contents:
        item = contents.pop(0)

        if item["type"] == "dir":
            contents.extend(get_repo_contents(item["path"]))

        elif item["type"] == "file" and item["name"].endswith(".py"):
            print(f"Reading: {item['path']}")

            file_response = requests.get(item["url"], headers=HEADERS)
            file_response.raise_for_status()
            file_data = file_response.json()

            decoded_code = base64.b64decode(
                file_data["content"]
            ).decode("utf-8")
            
            relative_path = item["path"].replace(f"{path}/", "")
            java_files[relative_path] = decoded_code
    
    if package_name:
        output_file = f"{package_name}.json"
    else:
        output_file=f"{path}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(java_files, f, indent=2, ensure_ascii=False)

    return java_files

def building_payload(
    file_content: dict,
    pipeline_id: int = 12658,
    user: str = "balamurugan.v@ascendion.com"
):
    payload = {
        "pipeLineId": pipeline_id,
        "executionId": str(uuid.uuid4()),
        "user": user,
        "userInputs": {},
        "priority":0
    }

    for idx, (filename, code) in enumerate(sorted(file_content.items()), start=1):
        key = f"{{{{python_code{idx}}}}}" 
        payload["userInputs"][key] = filename+":"+code
    print(payload)
    with open("payload.json","w") as f:
        f.write(json.dumps(payload))
    return payload

def send_request(payload):
    response = requests.post(
        url,
        json=payload,  
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "access-key": accessKey,
        },
        timeout=60
    )

    print("Status:", response.status_code)

    try:
        response_data = response.json()
    except Exception as e:
        print("JSON parsing failed even though status=200")
        print("Raw response:", response.text)
        raise e

    pipeline = response_data.get("pipeline", {})
    output = pipeline.get("output", "")
    print("\n")
    print(type(output))
    print("\n")
    folder = "AGNTSOUTPUT"
    os.makedirs(folder, exist_ok=True)

    agents = pipeline.get("pipeLineAgents", [])
    agent_name = agents[0]["agent"]["name"] if agents else "unknown_agent"

    file_path = os.path.join(folder, f"{agent_name}.json")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(output)

    print("Output written to:", file_path)
    return output


def parse_json():
    folder = "AGNTSOUTPUT"
    file_path = os.path.join(folder, "Python_Codebase_Version_Upgrade.json")
    with open(file_path,"r", encoding="utf-8") as f:
        data=json.load(f)
    py_files = {
        key: value
        for key, value in data.items()
        if isinstance(key, str) and key.endswith(".py")
    }
    return py_files


def get_file_sha(file_path):
    """Get the SHA of a file from the GitHub repository"""
    url = f"{BASE_URL}/repos/{REPO_NAME}/contents/{file_path}"
    params = {"ref": BRANCH}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()["sha"]


def write_to_github(updated_files_dict, start_path="backend", commit_message="Update Python files"):
    updated_files = []
    
    for relative_path, updated_code in updated_files_dict.items():
        try:
            file_path = f"{start_path}/{relative_path}"
            file_sha = get_file_sha(file_path)
            encoded_content = base64.b64encode(
                updated_code.encode("utf-8")
            ).decode("utf-8")

            update_payload = {
                "message": commit_message,
                "content": encoded_content,
                "sha": file_sha,
                "branch": BRANCH
            }
            
            update_url = f"{BASE_URL}/repos/{REPO_NAME}/contents/{file_path}"
            response = requests.put(
                update_url,
                json=update_payload,
                headers=HEADERS
            )
            response.raise_for_status()
            
            print(f"Successfully updated: {file_path}")
            updated_files.append(file_path)
            
        except Exception as e:
            print(f"Failed to update {relative_path}: {str(e)}")
    
    print(f"\nTotal files updated: {len(updated_files)}/{len(updated_files_dict)}")
    return updated_files

def main():
    file_content=grouping_fileContents_in_dict()
    PL=building_payload(file_content)
    send_request(payload=PL)
    python_dict=parse_json()
    print(python_dict)
    print("\n" + "="*50)
    print("Writing updated files back to GitHub...")
    print("="*50)
    write_to_github(python_dict)
  
if __name__ == "__main__":
    main()