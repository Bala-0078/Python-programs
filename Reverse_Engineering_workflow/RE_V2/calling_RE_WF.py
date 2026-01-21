import json
import requests
import uuid
from dotenv import load_dotenv
import os
load_dotenv()
accessKey=os.getenv("access_key")

url="https://avaplus-internal.avateam.io/force/platform/pipeline/api/v1/execute/files"

def send_request(headers, zip_file_path, payload=None):
    files = {
        "files": (
            "vitejs-vite-t6cepbz2 (1).zip",
            open(zip_file_path, "rb"),
            "application/zip"
        )
    }

    response = requests.post(
        url,
        data=payload,
        files=files,
        headers=headers
    )

    print("Status:", response.status_code)
    response_data=response.json()
    output=response_data.get("pipeline", {}).get("output", "")
  
    folder="RE_V2"
    pipeline_agents = response_data.get("pipeline", {}).get("pipeLineAgents", [])
    agent_name = pipeline_agents[0]["agent"]["name"]
    file_path = os.path.join(os.getcwd(), folder, agent_name + ".md")
    with open(file_path,"w",encoding="utf-8") as f:
        f.write(output)
    return output

def run_pipeline(pipeline_id, user_inputs, headers, zip_file_path, user_name):
    payload = {
        "executionId": str(uuid.uuid4()),
        "pipeLineId": pipeline_id,
        "user": user_name,
        "priority": "0",
        "userInputs": json.dumps(user_inputs)
    }
    return send_request(headers, zip_file_path, payload)

        
if __name__ == "__main__":
    headers = {
        "Accept": "application/json",
        "access-key": accessKey,
    }

    zip_file_path = "C:\\Users\\balamurugan.v\\Downloads\\vitejs-vite-t6cepbz2 (1).zip"
    user_name = "balamurugan.v@ascendion.com"

    WF1 = run_pipeline(
        "12391",
        {"%1$s": "vitejs-vite-t6cepbz2"},
        headers, zip_file_path, user_name
    )
    WF2 = run_pipeline(
        "12392",
        {"{{Input}}": json.dumps(WF1)},
        headers, zip_file_path, user_name
    )
    WF3 = run_pipeline(
        "12393",
        {
            "{{EE_Web_Folder_Structure_Extractor}}": WF1,
            "{{EE_Web_Framework_Detector}}": WF2
        },
        headers, zip_file_path, user_name
    )
    WF4 = run_pipeline(
        "12414",
        {
            "{{EE_Web_Folder_Structure_Extractor}}": WF1,
            "{{EE_Web_Framework_Detector}}": WF2,
            "{{EE_Web_Framework_Validator}}": WF3
        },
        headers, zip_file_path, user_name
    )
    WF5 = run_pipeline(
        "12416",
        {
            "{{EE_Web_Folder_Structure_Extractor}}": WF1,
            "{{EE_Web_Framework_Detector}}": WF2,
            "{{EE_Web_Framework_Validator}}": WF3,
            "{{EE_Web_Application_Structure_Analyzer}}": WF4
        },
        headers, zip_file_path, user_name
    )
    WF6 = run_pipeline(
        "12424",
        {
            "{{EE_Web_Folder_Structure_Extractor}}": WF1,
            "{{EE_Web_Framework_Detector}}": WF2,
            "{{EE_Web_Framework_Validator}}": WF3,
            "{{EE_Web_Application_Structure_Analyzer}}": WF4,
            "{{EE_Web_Application_Flow_Mapper}}": WF5
        },
        headers, zip_file_path, user_name
    )
    WF7 = run_pipeline(
        "12425",
        {
            "{{EE_Web_Folder_Structure_Extractor}}": WF1,
            "{{EE_Web_Framework_Detector}}": WF2,
            "{{EE_Web_Framework_Validator}}": WF3,
            "{{EE_Web_Application_Structure_Analyzer}}": WF4,
            "{{EE_Web_Application_Flow_Mapper}}": WF5,
            "{{EE_Web_Application_Dependency_Graph_Generator}}": WF6
        },
        headers, zip_file_path, user_name
    )
    WF8 = run_pipeline(
        "12426",
        {
            "{{EE_Web_Folder_Structure_Extractor}}": WF1,
            "{{EE_Web_Framework_Detector}}": WF2,
            "{{EE_Web_Framework_Validator}}": WF3,
            "{{EE_Web_Application_Structure_Analyzer}}": WF4,
            "{{EE_Web_Application_Flow_Mapper}}": WF5,
            "{{EE_Web_Application_Dependency_Graph_Generator}}": WF6,
            "{{EE_Web_Application_Architecture_Extractor}}": WF7
        },
        headers, zip_file_path, user_name
    )
    WF9 = run_pipeline(
        "12427",
        {
            "{{EE_Web_Folder_Structure_Extractor}}": WF1,
            "{{EE_Web_Framework_Detector}}": WF2,
            "{{EE_Web_Framework_Validator}}": WF3,
            "{{EE_Web_Application_Structure_Analyzer}}": WF4,
            "{{EE_Web_Application_Flow_Mapper}}": WF5,
            "{{EE_Web_Application_Dependency_Graph_Generator}}": WF6,
            "{{EE_Web_Application_Architecture_Extractor}}": WF7,
            "{{EE_Web_Technical_Documentation_Generator}}": WF8
        },
        headers, zip_file_path, user_name
    )
    print("All pipelines executed successfully")