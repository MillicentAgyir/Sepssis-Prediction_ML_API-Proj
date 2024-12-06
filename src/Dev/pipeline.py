import pickle

# Load saved components
with open('ml_components.pkl', 'rb') as file:
    components = pickle.load(file)

scaler = components['scaler']
model = components['model']

# Prediction function
def predict_sepsis(input_data):
    transformed_data = scaler.transform([input_data])
    prediction = model.predict(transformed_data)
    return prediction
