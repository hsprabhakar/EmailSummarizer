import json

def clean_llm_response(raw_content):
    if raw_content.startswith("```json"):
        raw_content = raw_content.strip("```json").strip("```")
    try:
        json_content = json.loads(raw_content)
        return json_content
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return {"error": "Failed to parse JSON response", "raw_content": raw_content}