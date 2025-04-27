from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import service

app = Flask(__name__, template_folder='frontend', static_folder='frontend', static_url_path='')
CORS(app)  # Enable CORS

@app.route('/')
def serve_frontend():
    """Serve the frontend HTML file"""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/profile')
def serve_frontend_profile():
    """Serve the frontend HTML file"""
    return send_from_directory(app.static_folder, 'profile.html')

@app.route('/api/data')
def get_data():
    """Return sample JSON data"""
    return jsonify({"message": "Hello from Flask!", "status": "success"})

@app.route('/api/create_profile', methods=['POST'])
def create_profile():
    profile_data = request.get_json()
    if not profile_data:
        return jsonify({"error": "Missing profile data"}), 400
    result = service.create_profile(profile_data)
    # Convert ObjectId to string if result is ObjectId
    if hasattr(result, '__str__'):
        result = str(result)
    return jsonify({"result": result})

@app.route('/api/update_profile', methods=['PUT'])
def update_profile():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Missing name or data"}), 400
    name = data['name']
    # Remove name from data to update other fields
    update_data = {k: v for k, v in data.items() if k != 'name'}
    update_results = {}
    for field, value in update_data.items():
        update_results[field] = service.update_field(name, field, value)
    return jsonify({"updated_fields": update_results})

@app.route('/api/get_profile', methods=['GET'])
def get_profile():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Missing name parameter"}), 400
    profile = {}
    # Retrieve all fields using service functions
    fields = [
        "bio", "profile_pic", "objective", "experience", "projects", "skills",
        "certifications", "internships", "education", "achievements", "research_work"
    ]
    for field in fields:
        getter = getattr(service, f"get_{field}", None)
        if getter:
            profile[field] = getter(name)
    profile["name"] = name
    return jsonify(profile)

@app.route('/api/list_profile', methods=['GET'])
# list profile will return list of names of the profiles
def list_profile_names():
    profiles_cursor = service.db.collection.find()
    profiles = []
    for profile in profiles_cursor:
        profile['_id'] = str(profile['_id'])
        profiles.append(profile['name'])
    return jsonify(profiles)

@app.route('/api/generate', methods=['POST'])
def generate_resume():
    data = request.get_json()
    if not data or 'job_post' not in data or 'name' not in data:
        return jsonify({"error": "Missing job_post or name in request body"}), 400
    job_post = data['job_post']
    name = data['name']
    # Retrieve profile data for the given name
    profile = {}
    fields = [
        "bio", "profile_pic", "objective", "experience", "projects", "skills",
        "certifications", "internships", "education", "achievements", "research_work"
    ]
    for field in fields:
        getter = getattr(service, f"get_{field}", None)
        if getter:
            profile[field] = getter(name)
    profile["name"] = name
    # Generate resume fields using AI service
    generated_resume_fields = service.generate_resume_for_profile(job_post, profile)
    # Join all generated fields into a single string
    complete_resume = "\n\n".join(generated_resume_fields.values())
    return jsonify({"resume": complete_resume})

from flask import Response
from io import BytesIO

@app.route('/api/download_pdf', methods=['POST'])
def download_pdf():
    data = request.get_json()
    if not data or 'resume_text' not in data:
        return jsonify({"error": "Missing resume_text in request body"}), 400
    resume_text = data['resume_text']
    pdf_bytes = service.generate_pdf_resume(resume_text)
    return Response(
        pdf_bytes,
        mimetype='application/pdf',
        headers={"Content-Disposition": "attachment;filename=resume.pdf"}
    )

@app.route('/api/download_docx', methods=['POST'])
def download_docx():
    data = request.get_json()
    if not data or 'resume_text' not in data:
        return jsonify({"error": "Missing resume_text in request body"}), 400
    resume_text = data['resume_text']
    docx_bytes = service.generate_docx_resume(resume_text)
    return Response(
        docx_bytes,
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        headers={"Content-Disposition": "attachment;filename=resume.docx"}
    )

if __name__ == '__main__':
    app.run(port=5500, debug=True)
