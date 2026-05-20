import pandas as pd
import pickle
import os

#Change working directory
#os.chdir(r"F:\Project\CareerTech_Mapper\Deployment")


# Load features and targets
X = pd.read_pickle('model/X_features.pkl')
y = pd.read_pickle('model/y_target.pkl')

# Load feature and target column names
feature_names = X.columns.to_list()
target_names = y.columns.to_list()

# Load trained model and optimized thresholds
trained_model = pickle.load(open('model/model.pkl', 'rb'))
optimal_thresholds = pickle.load(open('model/thresholds.pkl', 'rb'))




def suggest_careers(skills):

    """
    Predict most suitable careers based on input skills.
    """

    # Initialize input vector with zeros
    input_dict = dict.fromkeys(feature_names, 0)


    # Apply the same standarization but multiplied by 2 
    for feature in feature_names:
        input_dict[feature] = X[feature].min() * 2

    for skill in skills:
        input_dict[skill] = X[skill].max() * 2


    # Convert to DataFrame
    input_df =pd.DataFrame([input_dict])

    # Predict probabilities
    y_probs = trained_model.predict_proba(input_df )[0]

    # Apply optimal thresholds per label
    y_pred = (y_probs > optimal_thresholds).astype(int)


    # Create a results dataframe
    results_df  = pd.DataFrame({
        'career': target_names,
        'probability': y_probs, 
        'is_selected':y_pred
        })
    
    # Keep only predicted careers (apply threshold filter)
    results_df ['final_score'] = results_df ['probability']  * results_df ['is_selected']
    results_df  = results_df [results_df ['final_score'] > 0]

    # Sort careers by confidence (highest probability first)
    results_df  = results_df .sort_values(by='final_score', ascending=False)

    #List of predicted careers (sorted)
    predicted_careers = results_df ['career'].tolist()
    
    return predicted_careers





def get_career_prob(skills,career):

    """
    Return probability of a specific career given input skills.
    """

    # Initialize input vector with zeros
    input_dict = dict.fromkeys(feature_names, 0)


    # Set all features to their minimum values from training data
    for feature in feature_names:
        input_dict[feature] = X[feature].min() * 2

    # Activate provided skills using maximum values
    for skill in skills:
        input_dict[skill] = X[skill].max() * 2


    # Convert to DataFrame for model input
    input_df = pd.DataFrame([input_dict])

    # Get probability predictions for all careers
    probs = trained_model.predict_proba(input_df)[0]

    # Career index lookup
    career_idx=target_names.index(career)
    
    # Return probability of selected career    
    return probs[career_idx]





def get_impactful_skills(skills,career):

    """
    Suggest additional skills that improve probability of achieving a target career.
    """

    # Ensure we don't modify original input
    base_skills = list(set(skills))

    # Baseline probability with current skills
    base_prob = get_career_prob(skills,career) 

    results = []

    for feature in feature_names:

        # Skip if skill already exists
        if feature in base_skills:
            continue
        
        # Try adding the feature
        test_skills = base_skills + [feature]


        # Compute new probability
        new_prob = get_career_prob(test_skills,career)

        # Improvement percentage
        impact_precentage = (new_prob - base_prob) / base_prob


        # Keep only useful skills
        if impact_precentage > 0:
            results.append({
                'skill':feature,
                'probability_after':impact_precentage
            })

    # Convert to DataFrame
    results_df = pd.DataFrame(results)

    # Sort by most impactful skills
    results_df = results_df.sort_values(by="probability_after", ascending=False)


    impactful_skills = list(results_df['skill'].head(10))


    return impactful_skills




def get_related_skills(career, n=5, h=10):

    """
    Return the most related skills for a target career
    """


    # Initialize input vector with zeros
    input_dict = dict.fromkeys(feature_names, 0)

    predicted_skills=[]
    predicted_values=[]


    # Apply baseline representation (all skills is inactive)
    # n is scalar factor 
    for feature in feature_names:
        input_dict[feature] = X[feature].min() *n


    # Test each skill independently
    for skill in feature_names:

        # Activate current skill
        input_dict[skill] = X[skill].max() *n

        # Convert to DataFrame
        input_df =pd.DataFrame([input_dict])

        # Predict probabilities
        y_probs = trained_model.predict_proba(input_df )[0]



        # Create probability dataframe
        probs_df  = pd.DataFrame({
            'career': target_names,
            'probability': y_probs, 
            })
    

        # Sort careers by confidence (highest probability first)
        probs_df  = probs_df .sort_values(by='probability', ascending=False)

        # Get top (h) predicted careers
        probs_df = probs_df.head(h)

        # Check if target career exists in top (h) predictions
        if career in probs_df['career'].values:
            predicted_skills.append(skill)

            value = probs_df[probs_df['career']==career]['probability'].values[0]
            predicted_values.append(value)

        # Reset skill back to baseline
        input_dict[skill] = X[feature].min() *n

    
    # Build final results dataframe
    results_df = pd.DataFrame({
            'skill': predicted_skills,
            'probability': predicted_values
        })

    # Sort skills by probability
    results_df=results_df.sort_values(by='probability', ascending=False)

    # Adaptive recursion for weak careers
    if results_df.shape[0] < 12:
        return get_related_skills(career, n*2, h+1)
    
    # Return top related skills
    result = results_df['skill'].head(12)
    return list(result)




def suggest_more_skills(skills,career):

    """
    Suggest additional skills
    """
    if len(skills) < 7:
        related_skills = get_related_skills(career)

        # remove already known skills
        suggested_skills = list(set(related_skills) - set(skills))
        return suggested_skills

    else:   
        related_skills = get_related_skills(career)
        impactful_skills = get_impactful_skills(skills,career)

        # merge both sources
        total_skills = list(set(related_skills + impactful_skills))

        # remove already known skills
        suggested_skills = list(set(total_skills) - set(skills))
        return suggested_skills
    

