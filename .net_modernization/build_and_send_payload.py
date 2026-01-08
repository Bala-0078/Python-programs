import json
import requests
import uuid
from dotenv import load_dotenv
import os
load_dotenv()
accessKey=os.getenv("access_key")

REQUEST_URL = "https://avaplus-internal.avateam.io/force/platform/pipeline/api/v1/execute"
def read_file(path):
    with open(path, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    return text


def build_payload(legacy_content, modern_content, user, pipeline_id):
    user_inputs = {}
    if legacy_content:
        user_inputs["{{legacy_code}}"] = legacy_content
    if modern_content:
        user_inputs["{{modernized_code}}"] = modern_content
    payload = {
        "executionId": str(uuid.uuid4()),
        "pipeLineId": int(pipeline_id),
        "user": user,
        "userInputs": user_inputs,
        "priority": 0
    }
    return payload


def post_payload(payload, access_key):
    headers = {"accept": "application/json"}
    headers["access-key"] = access_key
    resp = requests.post(REQUEST_URL, headers=headers, json=payload)
    j = resp.json()
    with open("response.json", "w") as f:
        json.dump(j, f, indent=2)
    return resp.status_code, j

    

def main():
    legacy_path = "C:\\Users\\balamurugan.v\\Downloads\\.Net Legacy&Modern\\LegacyCustomerPortal\\service\\CustomerService.cs"
    modern_path = "C:\\Users\\balamurugan.v\\Downloads\\.Net Legacy&Modern\\ModernCustomerPortal\\service\\CustomerService.cs"
    user_email = "balamurugan.v@ascendion.com"
    pipeline_id = "11993"
    legacy_content = read_file(legacy_path)
    modern_content = read_file(modern_path)
    payload = build_payload(legacy_content, modern_content, user_email, pipeline_id)
    status, resp = post_payload(payload, access_key=accessKey)
    print(f"\nPOST status: {status}")
    print("Response:", json.dumps(resp, indent=2)[:500])

if __name__ == "__main__":
    main()