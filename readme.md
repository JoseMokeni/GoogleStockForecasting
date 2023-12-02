<!-- RUN INSTRUCTIONS -->

## Run Instructions

Before running the backend and the frontend, you also need to run the notebook on the root directory to generate the model.

### Run the server

`python backend/app.py`

### Run the frontend

`cd frontend && npm start`

<!-- before everything, install the requirements -->

## Install Requirements

### Install python requirements

`pip install -r requirements.txt`

### Install frontend requirements

`cd frontend && npm install`

### Fill cloudinary variables

In the file `backend/prediction.py:79` fill the variables `cloud_name`, `api_key` and `api_secret` with your cloudinary credentials.
