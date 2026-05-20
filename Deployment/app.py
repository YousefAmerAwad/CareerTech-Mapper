from flask import Flask, request, jsonify,  render_template
from utils import suggest_careers, suggest_more_skills, feature_names, target_names


app = Flask(__name__)



# Home route 
@app.route('/')
def home():
    return render_template("index.html",skills=feature_names, careers=target_names)



# Predict careers from skills
@app.route('/predict-careers', methods=['POST'])
def predict_careers():

    data = request.get_json()
    skills = data.get("skills", [])

    careers = suggest_careers(skills)

    return jsonify({
        "input_skills": skills,
        "predicted_careers": careers
    })


# Suggest more skills
@app.route('/recommend-skills', methods=['POST'])
def recommend_skills():

    data = request.get_json()
    skills = data.get("skills", [])
    career = data.get("career")

    recommended = suggest_more_skills(skills, career)

    return jsonify({
        "current_skills": skills,
        "career": career,
        "recommended_skills": recommended
    })


# Run server
if __name__ == '__main__':
    app.run(host="0.0.0.0")