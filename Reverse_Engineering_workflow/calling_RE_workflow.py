import json
import requests
import time
from dotenv import load_dotenv
import os
load_dotenv()
accessKey=os.getenv("access_key")

url="https://avaplus-internal.avateam.io/v1/api/instructions/ava/force/workflow-executions"
def send_request(headers,zip_file_path,payload):
    files = {
        "files": (
            "vitejs-vite-t6cepbz2.zip",
            open(zip_file_path, "rb"),
            "application/zip"
        )
    }
    response = requests.post(url, data=payload, files=files, headers=headers)
    return response

def get_result(execution_id):
    url = f"https://avaplus-internal.avateam.io/v1/api/instructions/ava/force/workflow-executions/{execution_id}/result"
    headers = {"access-key": accessKey}
    while True:
        resp = requests.get(url, headers=headers)
        resp_json = resp.json()
        status = resp_json.get("status") or resp_json.get("result", {}).get("status")
        print("Status:", status)
        if status == "SUCCESS":
            print("Workflow completed successfully!")
            return resp_json
        if status in ("FAILED", "ERROR"):
            raise Exception("Workflow failed")
        time.sleep(6)

def save_result(result_json):
    try:
        response_payload = json.loads(result_json["result"]["response"])
    except Exception as e:
        print("Could not decode response:", e)
        return
 
    pipeline_agents = response_payload.get("pipeLineAgents", [])
    tasks_outputs = response_payload.get("tasksOutputs", [])
 
    print("\nSaving agent outputs...\n")
 
    for agent in pipeline_agents:
        serial = agent["serial"]    
        agent_name = agent["agent"]["name"]
        index = serial - 1
        if index >= len(tasks_outputs):
            print(f"No output found for {agent_name}")
            continue
        raw_output = tasks_outputs[index].get("raw", "")
        filename = agent_name + ".md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(raw_output)
        print(f"Saved: {filename}")

if __name__ == "__main__":
    headers = {
    "Accept": "application/json",
    "access-key": accessKey,
    }
    zip_file_path="C:\\Users\\balamurugan.v\\Downloads\\vitejs-vite-t6cepbz2 (1).zip"
    payload={
        "pipelineId": "1012",
        "user": "balamurugan.v@ascendion.com",
        "priority": "0",
        "userInputs": json.dumps({
            "%1$s": "vitejs-vite-t6cepbz2",
            "{{Input}}": "vitejs-vite-t6cepbz2"
        })
    }
    response = send_request(headers,zip_file_path,payload)
    result = get_result(response.json()["workflowExecutionId"])
    save_result(result)