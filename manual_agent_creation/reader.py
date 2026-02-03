import os
import requests
import json

url="https://avaplus-internal.avateam.io/v1/api/admin/ava/force/collaborativeAgent"
url2="https://avaplus-internal.avateam.io/v1/api/admin/ava/force/level?levelNum=0&parentLvlId=-1"
access_key="eyJraWQiOiI1ZWZhM2IxNy1hZDU2LTQ4MDAtOGNhMC0yY2ZmZjQxNjQ1OGEiLCJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FzY2VuZGlvbi5jb20iLCJpZGVudGlmaWVyIjoiYXZhIy0qZ3B0IiwibmFtZSI6IkJhbGFtdXJ1Z2FuIFZhc3VkZXZhbiIsImVtYWlsIjoiYmFsYW11cnVnYW4udkBhc2NlbmRpb24uY29tIiwiaWF0IjoxNzQ1Mzk4MjEzLCJleHAiOjE3NzY5MzQyMTN9.rsxiFv9ksGFK1xQXHeRz9IjxleYL9KzU1Bp6TcxN52ofPF9AE2k4eESm8Vy4IyYF4-ZHhh4EWpZleVhA-p0vUA"
response=requests.get(url=url2,headers={"access-key":access_key,"Content-Type":"application/json","Accept":"application/json"})
print(f"Response status code: {response.status_code}")
folder="manual_agent_creation"
file_path = os.path.join(folder, "response.json")
with open(file_path,"w",encoding="utf-8") as f:
    json.dump(response.json(),f,indent=2,ensure_ascii=False)