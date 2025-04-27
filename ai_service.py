from model import UserProfileDB
from prompts import prompts

def llmCall(Promptinstructions: str, job_post: str, field_info) -> str:
    """
    Placeholder function to simulate a call to a language model (LLM).
    It takes prompt instructions, job post, and field info, and returns a formatted string.
    """
    # For now, just return a formatted string combining inputs
    return f"Generated resume field based on prompt: {Promptinstructions}, job post: {job_post}, field info: {field_info}"

def generate_resume_fields(job_post: str, profile_data: dict) -> dict:
    """
    Calls llmCall for each field in UserProfileDB fields with separate prompt instructions and field values.
    Returns a dictionary with field names as keys and generated resume field strings as values.
    """
    fields = [
        "bio", "profile_pic", "objective", "experience", "projects", "skills",
        "certifications", "internships", "education", "achievements", "research_work"
    ]
    generated_fields = {}
    for field in fields:
        field_value = profile_data.get(field, "")
        prompt = prompts.get(field, f"Generate resume content for the field '{field}'.")
        generated_fields[field] = llmCall(prompt, job_post, field_value)
    return generated_fields
