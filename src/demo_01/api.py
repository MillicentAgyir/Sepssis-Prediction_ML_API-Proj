from fastapi import FastAPI
import pickle
from pydantic import BaseModel

app = FastAPI()

# Load saved ML components
with open('src/Dev/ml_components.pkl', 'rb') as file:
    components = pickle.load(file)

scaler = components['scaler']
model = components['model']
selected_features = components['selected_features']

# Define input data structure using Pydantic
class PredictionInput(BaseModel):
    features: list

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Prediction endpoint
@app.post("/predict")
async def predict(input_data: PredictionInput):
    try:
        # Ensure input data has the correct shape
        if len(input_data.features) != len(selected_features):
            return {"error": f"Expected {len(selected_features)} features, but got {len(input_data.features)} features"}

        # Transform the input data using the scaler
        transformed_data = scaler.transform([input_data.features])
        
        # Make prediction using the model
        prediction = model.predict(transformed_data)
        
        return {"prediction": int(prediction[0])}
    except Exception as e:
        return {"error": str(e)}
