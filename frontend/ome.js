const API_BASE_URL = window.location.origin; // Dynamically gets current host

// Function to fetch profile names from /api/list_profile and populate dropdown
function fetchProfileNames() {
    fetch('/api/list_profile')
        .then(response => response.json())
        .then(data => {
            console.log("Fetched profiles from /api/list_profile:", data);
            updateDropdownMenu(data);
        })
        .catch(error => console.error("Error fetching profiles:", error));
}

function updateDropdownMenu(profiles) {
    console.log("Updating dropdown menu with profiles:", profiles);
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
    loadProfile(name);
}

function loadProfile(name) {
    fetch(`/api/get_profile?name=${encodeURIComponent(name)}`)
        .then(response => response.json())
        .then(profile => populateProfileFields(profile))
        .catch(error => console.error("Error loading profile:", error));
}

function populateProfileFields(profile) {
    const fields = ['bio', 'experience', 'projects', 'skills', 'education', 'certifications', 'internships', 'achievements', 'research_work'];
    fields.forEach(field => {
        const elem = document.getElementById(field);
        if (elem) {
            elem.value = profile[field] || '';
        }
    });
}

function createProfileWithDefaults(name) {
    const defaultProfile = {
        name: name,
        bio: "",
        profile_pic: "",
        objective: "",
        experience: [],
        projects: [],
        skills: [],
        certifications: [],
        internships: [],
        education: [],
        achievements: [],
        research_work: []
    };

    fetch('/api/create_profile', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(defaultProfile),
    })
        .then(response => response.json())
        .then(() => {
            alert(`Profile created for ${name}`);
            fetchProfileNames();
            selectName(name);
        })
        .catch(error => console.error("Error creating profile:", error));
}

function saveProfileChanges() {
    if (!selectedName) {
        alert('Please select a name first.');
        return;
    }
    const fields = ['bio', 'experience', 'projects', 'skills', 'education', 'certifications', 'internships', 'achievements', 'research_work'];
    const updateData = { name: selectedName };

    fields.forEach(field => {
        const elem = document.getElementById(field);
        updateData[field] = elem ? elem.value : '';
    });

    fetch('/api/update_profile', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(updateData),
    })
        .then(response => response.json())
        .then(() => {
            alert(`Profile updated for ${selectedName}`);
        })
        .catch(error => console.error("Error updating profile:", error));
}

// Attach event listeners after DOM content is loaded
document.addEventListener('DOMContentLoaded', () => {
    const addNameButton = document.getElementById('addNameButton');
    if (addNameButton) {
        addNameButton.addEventListener('click', () => {
            const newName = prompt("Enter new name:");
            if (newName) {
                createProfileWithDefaults(newName);
            }
        });
    } else {
        console.error("Add Name button not found");
    }

    const saveChangesButton = document.getElementById('saveChangesButton');
    if (saveChangesButton) {
        saveChangesButton.addEventListener('click', saveProfileChanges);
    } else {
        console.error("Save Changes button not found");
    }

    // Populate names on page load
    fetchProfileNames();
});
