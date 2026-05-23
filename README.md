# CareerTech-Mapper
An intelligent machine learning-powered web application that helps users explore technology career paths and understand the relationship between technical skills and IT jobs.<br>

The system predicts suitable careers based on current skills and recommends additional technologies required to achieve a target career path.<br>
<br>


## Problem Statement
Our (fictional) client is an IT educational institute. They have reached out to us has reach out with the following:<br>

“IT jobs and technologies keep evolving quickly. This makes our field to be one of the most interesting out there. But on the other hand, such fast development confuses our students. They do not know which skills they need to learn for which job.” <br>

 “Do I need to learn C++ to be a Data Scientist?” “Do DevOps and System admins use the same technologies?” “I really like JavaScript; can I use it in Data Analytics?” Those are some of the questions that our students ask. <br>
 
Could you please develop a data-driven solution for our students to answer such questions? They mostly want to understand the relationships between the jobs and the technologies.<br>
<br>


## Project Objectives
CareerTech-Mapper was developed to:
- Predict relevant tech careers based on user skills
- Suggest additional skills required for a target career.
- Discover relationships between technologies and jobs.
- Help students build clearer learning roadmaps.
- Assist students in career planning and skill development
- Provide an interactive and user-friendly recommendation system.<br>

 **Features**:
- **Career Prediction**: Users select their current technical skills, and the model predicts the most relevant careers
- **Skill Recommendation**: Users select a target career and receive additional recommended skills that improve their fit for that role.<br>
<br>


## Dataset
The project uses data derived from the annual Stack Overflow Developer Survey dataset.<br>
**Link**: <https://insights.stackoverflow.com/survey> <br>

The dataset contains information about:

- Developer roles
- Programming languages
- Frameworks
- Databases
- Platforms
- Tools and technologies

The data was processed into:
- Skills (Features)
- Roles (Targets)
<br>

## Machine Learning Approach
The project uses a multi-label classification approach where:

- **Input**: technical skills
- **Output**: one or multiple careers <br>
### ML Workflow
- Data cleaning and preprocessing
- Feature standardization
- Feature engineering
- Cross-validation and performance analysis
- Multi-label classification using Logistic Regression with One-vs-Rest strategy
- Probability prediction per career label
- Per-label threshold optimization
- Career ranking based on confidence scores
- Reverse model inference for more skills suggestion

<br>

## Deployment 
- Backend is built with **Flask** to serve the machine learning model.
- The trained model and thresholds are loaded at runtime to enable real-time predictions.
- Frontend (**HTML**) communicates with the Flask API using POST requests.
- The API returns predictions in JSON format for both career prediction and skill recommendation.
- The application is deployed using **PythonAnywhere**
<br>


##  Test Cases
### Scinario 1 :
Suppose a user has recently started learning data-related technologies and currently possesses the following skills:
[**Python**, **Pandas**, **SQL**] <br>
The user is unsure which IT career path best matches these skills and uses our system to explore suitable career options.<br>
Let's see what our sestem suggests. <br>

**Screenshot**:<br>
<img width="442" height="877" alt="image" src="https://github.com/user-attachments/assets/801ef4cf-502c-4669-ad78-7c4939a06a6d" />

The system analyzes the input skills and correctly predicts the most relevant career paths, focusing mainly on analytics and machine learning-related roles. <br>

Now, suppose the user selects “**Data scientist or machine learning specialist**” and wants to know the additional skills required for this career. Let’s see what the system suggests.<br>

Screenshot:<br>
<img width="450" height="400" alt="image" src="https://github.com/user-attachments/assets/9f754444-072c-4f45-a636-f34363fa22be" /> <br>
The system successfully identifies relevant career paths from basic data skills and recommends industry-relevant skills needed to reach that career 
<br>

---

### Scinario 2 :
Suppose a computer engineering student has mainly studied academic and low-level programming technologies during university courses and currently possesses the following skills: [**Assembly**, **C**, **Java**, **MongoDB**, **MySQL**, **SQL**] <br>
The student wants to explore which career paths best match this background and uses our system for guidance. <br>
Let’s see what the system suggests <br>

Screenshot: <br>
<img width="395" height="870" alt="image" src="https://github.com/user-attachments/assets/2972dfc1-8d5d-463f-8725-a973be955e9e" /> <br>
The results reflect the student’s strong foundation in systems programming, databases, and backend-related technologies. <br>

Now, suppose the student is interested in becoming a **Mobile Application Developer** and wants to know which additional skills should be learned to transition into this field. <br>
Let’s see what the system recommends. <br>

Screenshot: <br>
<img width="400" height="450" alt="image" src="https://github.com/user-attachments/assets/1f1fc3e4-07bc-4f94-9514-eac83c5dd60d" /> <br>
The system successfully recognizes the student’s foundation in backend and systems-related technologies and recommends modern mobile development technologies required for transitioning into mobile application development <br>

---

### Scinario 3 :

Suppose a user is interested in web development and currently possesses the following frontend-related skills: [**HTML/CSS**, **JavaScript**, **React.js**] <br>
The user wants to discover which IT career paths best match these skills and uses the system for guidance. <br>
Let’s see what the system suggests. <br>

Screenshot: <br>
<img width="380" height="841" alt="image" src="https://github.com/user-attachments/assets/b3a6d178-3a1f-437b-ad36-67c8bbc74e7c" /> <br>
The results correctly reflect the user's strong frontend development background and UI-oriented technologies. <br>

Now, suppose the user wants to become a **Front-End Developer** and is looking for additional skills that could improve their profile. <br>
Let’s see what the system recommends.<br>

Screenshot: <br>
<img width="400" height="450" alt="image" src="https://github.com/user-attachments/assets/0848a8e3-bc25-4fef-87b6-c6848c24d1be" /> <br>
The system successfully recognizes the user’s focus on UI and front-end development and suggests additional technologies that expand frontend development capabilities






