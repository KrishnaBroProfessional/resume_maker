import requests
import json
from model import UserProfileDB
from prompts import prompts
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

api_token = os.getenv("API_TOKEN")
print(api_token)


def llmCall(Promptinstructions: str, job_post: str, field_info) -> str:
    """
    Calls the external API to get a completion response based on the prompt instructions, job post, and field info.
    """
    url = "https://api.lab45.ai/v1.1/skills/completion/query"
    print("Prompt instructions:", Promptinstructions)
    messages = [
        {
            "content": f"you are a resume generator AI. You will be given a job post and a field info. You need to generate the content for the field info based on the job post. Refer the example for format structure and beautify it , for example use # for heading. Make sure the year or timeline always align in right side using tabs. Do not add any extra information. {Promptinstructions}",
            "role": "system"
        },
        {
            "content": f" Job post: {job_post} Field info: {field_info}",
            "role": "user"
        }
    ]
    print(messages)
    payload = json.dumps({
        "messages": messages,
        "skill_parameters": {
            "emb_type": "openai",
            "model_name": "gpt-4o",#gemini-1.5-pro",
            "temperature": 0.3,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "retrieval_chain": "langchain",
            "top_k": 5,
            "top_p": 1
        },
        "stream_response": False
    })

    headers = {
        'Authorization': 'Bearer '+api_token,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # Parse JSON response and return only the content field if present
    try:
        dataa = response.json()
        print(dataa['data']['content'])
        content = dataa['data']['content'] or " " #response_json.get("data", {}).get("content", "")
        #print(content)
        return content
    except Exception:
        # Fallback to raw text if JSON parsing fails
        return response.text

def generate_resume_fields(job_post: str, profile_data: dict) -> dict:
    """
    Calls llmCall for each field in UserProfileDB fields with separate prompt instructions and field values.
    Returns a dictionary with field names as keys and generated resume field strings as values.
    """
    fields = [
        "bio", "objective", "experience", "projects", "skills",
        "certifications", "internships", "education", "achievements"
    ]
    generated_fields = {}
    for field in fields:
        field_value = profile_data.get(field, "")
        print("Field value:", field_value)
        prompt = prompts.get(field, f"Generate resume content for the field '{field}'.")
        generated_fields[field] = llmCall(prompt, job_post, field_value)
    return generated_fields
