import requests
import uuid
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")

EXECUTE_URL = "https://avaplus-internal.avateam.io/force/platform/pipeline/api/v1/execute/"
ACCESS_KEY = "eyJraWQiOiI1ZWZhM2IxNy1hZDU2LTQ4MDAtOGNhMC0yY2ZmZjQxNjQ1OGEiLCJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FzY2VuZGlvbi5jb20iLCJpZGVudGlmaWVyIjoiYXZhIy0qZ3B0IiwibmFtZSI6IkJhbGFtdXJ1Z2FuIFZhc3VkZXZhbiIsImVtYWlsIjoiYmFsYW11cnVnYW4udkBhc2NlbmRpb24uY29tIiwiaWF0IjoxNzQ1Mzk4MjEzLCJleHAiOjE3NzY5MzQyMTN9.rsxiFv9ksGFK1xQXHeRz9IjxleYL9KzU1Bp6TcxN52ofPF9AE2k4eESm8Vy4IyYF4-ZHhh4EWpZleVhA-p0vU"

PIPELINE_ID = "11950"
USER_EMAIL = "balamurugan.v@ascendion.com"
TARGET_URL = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"


html_response = requests.get(TARGET_URL, verify=False).text
soup = BeautifulSoup(html_response, "html.parser")

html_content = soup.prettify()

execution_id = str(uuid.uuid4())

headers = {
    "access-key": ACCESS_KEY,
    "accept": "application/json",
    "content-type": "application/json"
}

payload = {
    "pipeLineId": PIPELINE_ID,
    "user": USER_EMAIL,
    "executionId": execution_id,
    "priority": 0,
    "userInputs": {
        "{{inputFile}}": html_content
    }
}

response = requests.post(
    EXECUTE_URL,
    headers=headers,
    json=payload
)

response.raise_for_status()

response_json = response.json()
output_response = response_json.get("pipeline", {}).get("output", "")

print("Pipeline output:")
print(output_response)
