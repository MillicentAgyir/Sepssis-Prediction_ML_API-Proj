
<<<<<<< HEAD
# Machine Learning API using FastAPI
## Overview
=======
# Sepssis-Prediction_ML_API-Proj
Develop a Machine Learning API (Application Programming Interface) using FastAPI.
>>>>>>> 5e7d8af28faf13a6a0b20b09f40be1871be252f5

This project is a machine learning API built to predict sepsis based on patient data. It uses a trained classification model deployed as a REST API using FastAPI. The prediction model helps healthcare professionals assess the risk of sepsis by entering key health metrics.



## Features

i. Predict whether a patient is at risk of sepsis based on input data.

ii. API endpoints for submitting patient data and getting predictions.

iii.Built with FastAPI for high performance and easy usage.

iv. Swagger UI for easy interaction and testing of endpoints.

v. Dockerized to make deployment easy and consistent.



## Setup Instructions

### Prerequisites

- Python 3.8 or higher

- Docker (optional, for containerized deployment)

- Git


### Local Setup

1. Clone the Repository

  git clone https://github.com/MillicentAgyir/Sepssis-Prediction_ML_API-Proj.git
  cd Sepssis-Prediction_ML_API-Proj

2. Install Dependencies : Make sure you are in the project directory and then run:

   pip install -r requirements.txt

3. Run the API : To start the FastAPI server locally, run the following command:

   uvicorn api:app --reload

The API will be accessible at: http://127.0.0.1:8000

Swagger UI (for API testing) is available at: http://127.0.0.1:8000/docs


## Docker Setup

1. Build the Docker Image





## Rubrics

Machine Learning :

-   **Excellent:** Have a pipeline/function that takes inputs and make accurate predictions.

-   **Good:** Have a pipeline/function that takes inputs and make predictions.

-   **Fair:** Have a pipeline/function that takes inputs but faces bugs while doing predictions.

API :

-   **Excellent:** Have an API that works correctly, taking inputs multiple inputs and returning all the related predictions.

-   **Good:** Have an API that launches, makes predictions and returns results.

-   **Fair:** Have an API that launches but having bugs regarding inputs handling or returning predictions.

## Setup

Install the required packages to be able to run the evaluation locally.

You need to have [`Python 3`](https://www.python.org/) on your system (**a Python version lower than 3.10**). Then you can clone this repo and being at the repo's `root :: repository_name> ...`  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

The both long command-lines have a same structure, they pipe multiple commands using the symbol ` ; ` but you may manually execute them one after another.

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that it will be allow to import them into the python's scripts and notebooks without any issue.

**NB:** For MacOs users, please install `Xcode` if you have an issue.

## Run FastAPI

- Run the demo apps (being at the repository root):
        
  FastAPI:
    
    - Demo

          uvicorn src.demo_01.api:app --reload 

    <!-- - Salary prediction

          uvicorn src.salary.api:app --reload  -->


  - Go to your browser at the following address, to explore the api's documentation :
        
      http://127.0.0.1:8000/docs


<!-- ## Screenshots

<table>
    <tr>
        <th>FastAPI</th>
        <th>FastAPI</th>
    </tr>
    <tr>
        <td><img src="./screenshots/.png"/></td>
        <td><img src="./screenshots/.png"/></td>
    </tr>
</table> -->


## Resources
Here are some ressources you would read to have a good understanding of FastAPI :
- [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
- [Video - Building a Machine Learning API in 15 Minutes ](https://youtu.be/C82lT9cWQiA)
- [FastAPI for Machine Learning: Live coding an ML web application](https://www.youtube.com/watch?v=_BZGtifh_gw)
- [Video - Deploy ML models with FastAPI, Docker, and Heroku ](https://www.youtube.com/watch?v=h5wLuVDr0oc)
- [FastAPI Tutorial Series](https://www.youtube.com/watch?v=tKL6wEqbyNs&list=PLShTCj6cbon9gK9AbDSxZbas1F6b6C_Mx)
- [Http status codes](https://www.linkedin.com/feed/update/urn:li:activity:7017027658400063488?utm_source=share&utm_medium=member_desktop)





## Contributing

Feel free to make a PR or report an issue 😃.

Oh, one more thing, please do not forget to put a description when you make your PR 🙂.

## Author

- [Emmanuel KOUPOH](https://www.linkedin.com/in/esa%C3%AFe-alain-emmanuel-dina-koupoh-7b974a17a/)
[![My Twitter Link](https://img.shields.io/twitter/follow/emmanuelkoupoh?style=social)](https://twitter.com/emmanuelkoupoh)
=======

>>>>>>> f715ae4b1b971e5707938a4f7d9d983806c1557d
