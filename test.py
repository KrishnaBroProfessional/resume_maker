
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

# # Insert profile
# insert_response = db.create_profile(new_profile)
# print(f"Insertion Response: {insert_response}")

# Insert profile (if needed)
db.collection.insert_one(profile_data)

# Update a specific field
db.set_bio(name, "Lead AI Engineer specializing in deep learning.")

# Retrieve individual fields
print("Bio:", db.get_bio(name))
print("Objective:", db.get_objective(name))

# Update another field
db.set_education(name, "PhD in Artificial Intelligence")

# Get updated education
print("Education:", db.get_education(name))

# Retrieve all profiles
profiles = db.collection.find()
print("All Profiles:")
for profile in profiles:
    print(profile)