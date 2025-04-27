# Resume Maker
We will use this repo to maintian the code of AI resume maker.

## Why ?
To create custom resumes based on job posting requirements.

## Requirements :

- Defining resume sections
- Gathering data based on sections
- Identify apt. AI model and integrate it with apt. prompt instructions with sample resume format
- Use lib to convert md to docx
- Get basic frontend where you can input the job post desc and username(Krishna / Arjun). We need to add few more panels to update our skills and exp.
- Auto job application bot < Next step >

## Perchance Version

I have tried implementing simple similar resume maker using perchance.

### Cons :

 * can't automate it further.
 * publicly accessible

--- requires lil docs reference

## Flask application

### Steps

- ### Mongo DB setup
    - ``[{name:"ARJUN",... }]``
    - Planned fields :
        - BIO
            - Name
            - Email
            - Location
            - role
            - Phone
            - Linkedin
        - Objective
            - key objective
        - Experience
            - Company Name
            - role
            - timeline
            - work description
        - Projects
        - Skills & Abilities
            - Techinical skills
            - soft skills
        - Certifications & Accreditations
            -  list of all the certifications
        - Internships
            - Org name
            - timeline
            - tasks desc.
        - Education
            - degree name
            - position
            - year of completion
            - university/board name
        - Achievements
            - list all the awards here
        - Research Work < Optional >
 - ### UI Design
    - ### Home Page
        - Name Dropdown
        - Input TextArea for job positing desc
        - [Right Side] Generated Resume
        - Download Docx button
        - Preview PDF button
    - ### Profile Page
        - Name Dropdown with + icon to the right
        - Sections for Bio, Experience, Projects, Skills, and Education
        - Save Changes button





### Images

[bg](https://images.squarespace-cdn.com/content/v1/580789c229687f2f9402d360/1624434344107-4NGMTLWNOYNRGFPTW5L3/Elements+Item+D.gif)

[bg1](https://i.gifer.com/ENjk.gif)

[bg2](https://cdna.artstation.com/p/assets/images/images/016/265/566/original/mikhail-gorbunov-ui-1.gif?1551525784)
