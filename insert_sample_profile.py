import service

def main():
    sample_profile = {
        "name": "John Doe",
        "bio": "Software developer with 5 years of experience in web development.",
        "profile_pic": "https://example.com/johndoe.jpg",
        "objective": "To obtain a challenging position in a reputable organization.",
        "experience": [
            {"company": "Tech Corp", "role": "Senior Developer", "years": 3},
            {"company": "Web Solutions", "role": "Developer", "years": 2}
        ],
        "projects": ["Project A", "Project B"],
        "skills": ["Python", "JavaScript", "MongoDB", "Flask"],
        "certifications": ["Certified Python Developer"],
        "internships": ["Intern at Startup Inc."],
        "education": ["BSc Computer Science"],
        "achievements": ["Employee of the Year 2022"],
        "research_work": ["Research on scalable web applications"]
    }

    result = service.create_profile(sample_profile)
    if isinstance(result, str):
        print(f"Error: {result}")
    else:
        print(f"Sample profile inserted with id: {result}")

if __name__ == "__main__":
    main()
