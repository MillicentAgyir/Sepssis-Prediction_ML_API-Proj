from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from typing import List

# Load the saved ML components
with open('src/Dev/ml_components.pkl', 'rb') as file:
    components = pickle.load(file)

scaler = components['scaler']
model = components['model']

# Initialize FastAPI
app = FastAPI()

# Define input data structure using Pydantic
class PatientData(BaseModel):
    PRG: int  # Number of pregnancies
    PL: int   # Plasma glucose concentration
    PR: int   # Diastolic blood pressure (mm Hg)
    SK: int   # Triceps skinfold thickness (mm)
    TS: int   # 2-Hour serum insulin (mu U/ml)
    M11: float  # BMI (Body Mass Index)
    BD2: float  # Diabetes pedigree function
    Age: int   # Age (years)
    Insurance: bool  # Whether or not the patient has insurance (True/False)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Sepssis Prediction API!"}

# Prediction endpoint for multiple inputs
@app.post("/predict")
async def predict(patient_data_list: List[PatientData]):
    try:
        predictions = []

        # Iterate over each patient's data and make predictions
        for patient_data in patient_data_list:
            # Convert the patient data to a list of features
            features = [
                patient_data.PRG, patient_data.PL, patient_data.PR,
                patient_data.SK, patient_data.TS, patient_data.M11,
                patient_data.BD2, patient_data.Age, patient_data.Insurance
            ]

            # Convert features to a numpy array and reshape for prediction
            features_array = np.array(features).reshape(1, -1)

            # Scale the features using the saved scaler
            transformed_data = scaler.transform(features_array)

            # Make a prediction using the trained model
            prediction = model.predict(transformed_data)

            # Convert prediction to human-readable output
            prediction_label = "Positive" if prediction[0] == 1 else "Negative"

            # Append the prediction to the results list
            predictions.append({
                "input": patient_data.dict(),
                "prediction": prediction_label
            })

        # Return all predictions
        return {"predictions": predictions}
    
    except Exception as e:
        return {"error": str(e)}

# Run with `uvicorn api:app --reload`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
