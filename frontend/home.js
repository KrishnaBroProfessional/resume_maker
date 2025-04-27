const API_BASE_URL = window.location.origin; // Dynamically gets current host

// Function to fetch profile names from /api/list_profile and populate dropdown
function fetchProfileNames() {
    fetch('/api/list_profile')
        .then(response => response.json())
        .then(data => {
            updateDropdownMenu(data);
        })
        .catch(error => console.error("Error fetching profiles:", error));
}

function updateDropdownMenu(profiles) {
    const menu = document.getElementById('nameDropdownMenu');
    if (!menu) {
        console.error("Dropdown menu element not found");
        return;
    }
    menu.innerHTML = ''; // Clear existing items
    profiles.forEach(profileName => {
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.className = 'dropdown-item';
        a.href = '#';
        a.textContent = profileName;
        a.addEventListener('click', (event) => {
            event.preventDefault();
            selectName(profileName);
        });
        li.appendChild(a);
        menu.appendChild(li);
    });
}

let selectedName = null;

function selectName(name) {
    selectedName = name;
    const dropdownButton = document.getElementById("nameDropdown");
    if (dropdownButton) {
        dropdownButton.textContent = name;
    }
}

// Generate resume button
function generateResume() {
    if (!selectedName) {
        alert('Please select a name.');
        return;
    }
    const jobPostTextarea = document.getElementById('jobPostingTextarea');
    const resumeTextarea = document.getElementById('resumeTextarea');

    if (!jobPostTextarea.value.trim()) {
        alert('Please enter the job posting.');
        return;
    }

    fetch('/api/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: selectedName,
            job_post: jobPostTextarea.value.trim()
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.resume) {
            resumeTextarea.value = data.resume;
        } else {
            alert('Failed to generate resume.');
        }
    })
    .catch(error => {
        alert('Error generating resume: ' + error.message);
    });
}

// Download resume as plain text
function downloadResume() {
    const resumeTextarea = document.getElementById('resumeTextarea');
    if (!resumeTextarea.value.trim()) {
        alert('No resume content to download.');
        return;
    }
    const blob = new Blob([resumeTextarea.value], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'resume.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// Download resume as PDF
function downloadResumePDF() {
    const resumeTextarea = document.getElementById('resumeTextarea');
    if (!resumeTextarea.value.trim()) {
        alert('No resume content to download.');
        return;
    }
    fetch('/api/download_pdf', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ resume_text: resumeTextarea.value })
    })
    .then(response => {
        if (!response.ok) throw new Error('Failed to download PDF');
        return response.blob();
    })
    .then(blob => {
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'resume.pdf';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    })
    .catch(error => alert('Error downloading PDF: ' + error.message));
}

// Download resume as DOCX
function downloadResumeDOCX() {
    const resumeTextarea = document.getElementById('resumeTextarea');
    if (!resumeTextarea.value.trim()) {
        alert('No resume content to download.');
        return;
    }
    fetch('/api/download_docx', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ resume_text: resumeTextarea.value })
    })
    .then(response => {
        if (!response.ok) throw new Error('Failed to download DOCX');
        return response.blob();
    })
    .then(blob => {
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'resume.docx';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    })
    .catch(error => alert('Error downloading DOCX: ' + error.message));
}

// Attach event listeners after DOM content is loaded
document.addEventListener('DOMContentLoaded', () => {
    const generateResumeButton = document.getElementById('generateResumeButton');
    if (generateResumeButton) {
        generateResumeButton.addEventListener('click', generateResume);
    } else {
        console.error("Generate Resume button not found");
    }

    const downloadResumeButton = document.getElementById('downloadResumeButton');
    if (downloadResumeButton) {
        downloadResumeButton.addEventListener('click', downloadResume);
    } else {
        console.error("Download Resume button not found");
    }

    // Add buttons for PDF and DOCX download if not present
    let pdfButton = document.getElementById('downloadPDFButton');
    if (!pdfButton) {
        pdfButton = document.createElement('button');
        pdfButton.id = 'downloadPDFButton';
        pdfButton.textContent = 'Download PDF';
        pdfButton.className = 'btn btn-success mt-4 ms-2';
        const container = downloadResumeButton ? downloadResumeButton.parentNode : null;
        if (container) {
            container.appendChild(pdfButton);
            pdfButton.addEventListener('click', downloadResumePDF);
        }
    }

    let docxButton = document.getElementById('downloadDOCXButton');
    if (!docxButton) {
        docxButton = document.createElement('button');
        docxButton.id = 'downloadDOCXButton';
        docxButton.textContent = 'Download DOCX';
        docxButton.className = 'btn btn-success mt-4 ms-2';
        const container = downloadResumeButton ? downloadResumeButton.parentNode : null;
        if (container) {
            container.appendChild(docxButton);
            docxButton.addEventListener('click', downloadResumeDOCX);
        }
    }

    // Populate names on page load
    fetchProfileNames();
});
