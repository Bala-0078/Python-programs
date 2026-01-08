import json
import re

with open("response.json", "r", encoding="utf-8") as f:
    response = json.load(f)
output_text = response["pipeline"]["output"]
match = re.search(
    r'(\{\s*"comparison"\s*:\s*\{.*?\}\s*,\s*"summary_statistics"\s*:\s*\{.*?\}\s*\})',
    output_text,
    re.DOTALL
)

if not match:
    raise ValueError("Valid audit JSON block not found")

raw_json_block = match.group(1)
parsed_json = json.loads(raw_json_block)
formatted_json = json.dumps(parsed_json, indent=2, ensure_ascii=False)

with open("CustomerService_MigrationAudit.json", "w", encoding="utf-8") as f:
    f.write(formatted_json)