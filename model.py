from pymongo import MongoClient

class UserProfileDB:
    def __init__(self, connection_string, db_name="user_profiles", collection_name="profiles"):
        """Initialize MongoDB connection"""
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def update_field(self, name, field, value):
        """Update only the specified field for a profile"""
        result = self.collection.update_one({"name": name}, {"$set": {field: value}})
        return result.modified_count > 0  # Returns True if updated, False otherwise

    def get_field(self, name, field):
        """Retrieve a specific field value for a profile"""
        profile = self.collection.find_one({"name": name}, {field: 1, "_id": 0})
        return profile.get(field, "Field not found") if profile else "Profile not found"

    def set_bio(self, name, bio):
        return self.update_field(name, "bio", bio)

    def get_bio(self, name):
        return self.get_field(name, "bio")

    def set_profile_pic(self, name, profile_pic):
        return self.update_field(name, "profile_pic", profile_pic)

    def get_profile_pic(self, name):
        return self.get_field(name, "profile_pic")

    def set_objective(self, name, objective):
        return self.update_field(name, "objective", objective)

    def get_objective(self, name):
        return self.get_field(name, "objective")

    def set_experience(self, name, experience):
        return self.update_field(name, "experience", experience)

    def get_experience(self, name):
        return self.get_field(name, "experience")

    def set_projects(self, name, projects):
        return self.update_field(name, "projects", projects)

    def get_projects(self, name):
        return self.get_field(name, "projects")

    def set_skills(self, name, skills):
        return self.update_field(name, "skills", skills)

    def get_skills(self, name):
        return self.get_field(name, "skills")

    def set_certifications(self, name, certifications):
        return self.update_field(name, "certifications", certifications)

    def get_certifications(self, name):
        return self.get_field(name, "certifications")

    def set_internships(self, name, internships):
        return self.update_field(name, "internships", internships)

    def get_internships(self, name):
        return self.get_field(name, "internships")

    def set_education(self, name, education):
        return self.update_field(name, "education", education)

    def get_education(self, name):
        return self.get_field(name, "education")

    def set_achievements(self, name, achievements):
        return self.update_field(name, "achievements", achievements)

    def get_achievements(self, name):
        return self.get_field(name, "achievements")

    def set_research_work(self, name, research_work):
        return self.update_field(name, "research_work", research_work)

    def get_research_work(self, name):
        return self.get_field(name, "research_work")

    def create_profile(self, profile_data):
        existing_profile = self.collection.find_one({"name": profile_data.get("name")})
        if existing_profile:
            return "Profile with this name already exists!"
        return self.collection.insert_one(profile_data).inserted_id
