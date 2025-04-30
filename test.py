from model import UserProfileDB

# Initialize DB connection
MONGO_CONNECTION_STRING = ""
db = UserProfileDB(MONGO_CONNECTION_STRING)

# Example Usage
name = "John Doe"

# Insert Example Profile Data
profile_data = {
    "name": name,
    "bio": "Experienced AI Engineer passionate about innovation.",
    "profile_pic": "profile_picture_url",
    "objective": "To revolutionize AI-driven solutions.",
    "experience": "5+ years in software development.",
    "projects": "AI chatbot, predictive modeling, automation tools.",
    "skills": "Python, Machine Learning, Cloud Computing.",
    "certifications": "AWS Certified Solutions Architect.",
    "internships": "AI Research Internship at XYZ Corp.",
    "education": "Master's in Computer Science.",
    "achievements": "Best AI Innovation Award.",
    "research_work": "Published research on NLP advancements."
}

# Insert profile (if not exists)
insert_response = db.create_profile(profile_data)
print(f"Insertion Response: {insert_response}")

# Update a specific field
updated = db.set_bio(name, "Lead AI Engineer specializing in deep learning.")
print(f"Bio updated: {updated}")

# Retrieve individual fields
print("Bio:", db.get_bio(name))
print("Objective:", db.get_objective(name))

# Update another field
updated_education = db.set_education(name, "PhD in Artificial Intelligence")
print(f"Education updated: {updated_education}")

# Get updated education
print("Education:", db.get_education(name))

# Retrieve all profiles
profiles = db.collection.find()
print("All Profiles:")
for profile in profiles:
    print(profile)
