import joblib
import pandas as pd 

# Load the saved model from the file
knn_model = joblib.load('Model/knn_model.joblib')
# Assuming you have a new example with features (key length and presence of numbers)

def predict_key_power(string_len,has_number:bool):
    new_example = pd.DataFrame([[string_len, has_number]], columns=['Length', 'Contains Numbers Binary'])
    predicted_power_status = knn_model.predict(new_example)
    return predicted_power_status
