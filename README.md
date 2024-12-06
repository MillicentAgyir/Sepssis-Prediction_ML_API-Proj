# Sepsis Prediction API

## Overview
This project is a **machine learning API** built to predict sepsis based on patient data. It uses a trained classification model deployed as a REST API using **FastAPI**. The prediction model helps healthcare professionals assess the risk of sepsis by entering key health metrics.

The project contains all necessary components, including training code, the deployed application, Docker containerization, and API endpoints. This README will guide you through the setup and use of the API.

## Features
- Predict whether a patient is at risk of **sepsis** based on input data.
- API endpoints for submitting patient data and getting predictions.
- Built with **FastAPI** for high performance and easy usage.
- **Swagger UI** for easy interaction and testing of endpoints.
- **Dockerized** to make deployment easy and consistent.

## Setup Instructions
### Prerequisites
- Python 3.8 or higher
- Docker (optional, for containerized deployment)
- Git

### Local Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/MillicentAgyir/Sepssis-Prediction_ML_API-Proj.git
   cd Sepssis-Prediction_ML_API-Proj
   ```

2. **Install Dependencies**
   Make sure you are in the project directory and then run:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the API**
   To start the FastAPI server locally, run the following command:
   ```sh
   uvicorn api:app --reload
   ```
   - The API will be accessible at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - **Swagger UI** (for API testing) is available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Docker Setup
1. **Build the Docker Image**
   ```sh
   docker build -t sepssis-prediction-app .
   ```

2. **Run the Docker Container**
   ```sh
   docker run -p 8000:8000 sepssis-prediction-app
   ```

3. **Access the API**
   - The API will be available at: [http://localhost:8000](http://localhost:8000)
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

## API Endpoints
### `/predict`
- **Method**: `POST`
- **Description**: Takes patient attributes as input and returns a prediction of whether the patient is at risk of sepsis.
- **Input Format**:
  ```json
  {
    "PRG": 2,
    "PL": 120,
    "PR": 70,
    "SK": 3,
    "TS": 15,
    "M11": 0,
    "BD2": 1,
    "Age": 45,
    "Insurance": true
  }
  ```
- **Output Format**:
  ```json
  {
    "prediction": "Positive"
  }
  ```

## Screenshots
- **Swagger UI**: <img width="959" alt="image" src="https://github.com/user-attachments/assets/2f387711-c524-48f1-afc1-d2b4a2d4f026">

- **API Response Example**: <img width="897" alt="image" src="https://github.com/user-attachments/assets/9a4a8a79-8c6c-46cf-9417-455ce8fe2c86">

## Author
**Millicent Ama Agyir**
- GitHub: [MillicentAgyir](https://github.com/MillicentAgyir)
- Email: [agyirnana@gmail.com](mailto:agyirnana@gmail.com)

## Deployment
- **Deployed Application**: The app is available at: [https://dashboard.render.com/web/srv-ct9cpapu0jms73cpdkdg](https://dashboard.render.com/web/srv-ct9cpapu0jms73cpdkdg)
- **Swagger UI**: [https://sepssis-prediction-ml-api-proj.onrender.com/docs](https://sepssis-prediction-ml-api-proj.onrender.com/docs)
- **DockerHub Image**: The Docker image is available at [DockerHub](https://hub.docker.com/r/millicentagyir/sepssis-prediction-app)

## How to Use
1. **Clone the Repo** and set up your environment using the instructions above.
2. **Run the API** locally or using Docker.
3. Access the **Swagger UI** to test the API or use **Postman**.
4. **Deploy** the application to a cloud service like Render for broader access.

## License
This project is open-source and available under the **MIT License**.

## Acknowledgments
- Thanks to the Azubi Team for their guidance in making this project a success.

