IrisInsight – Iris Flower Species Classification using Machine Learning

Live Application:
https://codealpha-irisinsight.onrender.com

Overview

IrisInsight is a full-stack machine learning web application that classifies Iris flowers into three species — Setosa, Versicolor, and Virginica — based on their botanical measurements.

The project demonstrates an end-to-end ML workflow, from data preprocessing and model training to real-time inference through a deployed web interface.

Problem Statement

Accurately identifying Iris flower species based on physical characteristics is a classic supervised learning problem.
The objective of this project is to:

Train a classification model using the Iris dataset

Accept real-time user input via a web interface

Predict the species with high accuracy

Deploy the solution for public access

Dataset

Source: Iris Flower Dataset

Features Used:

Sepal Length (cm)

Sepal Width (cm)

Petal Length (cm)

Petal Width (cm)

Target Variable: Iris Species

Machine Learning Approach

Model Type: Supervised Classification

Algorithm: Scikit-learn classifier

Data Processing:

Feature selection

Label encoding

Model training and evaluation

Inference: Real-time prediction using trained model artifacts

Web Application Architecture
Frontend

HTML5

Tailwind CSS

JavaScript (Fetch API for asynchronous requests)

Backend

Flask (Python)

Joblib for model serialization

REST API for prediction endpoint

Deployment

Hosted on Render

Production server using Gunicorn

Absolute path handling for model loading

Application Workflow

User enters flower measurements through the web interface

Data is sent to the Flask backend via a POST request

The trained ML model processes the input

Predicted species (and confidence, if available) is returned

Result is displayed dynamically on the page

Project Structure
CodeAlpha_IrisInsight/
│
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│   ├── iris_model.pkl
│   └── label_encoder.pkl
│
├── data/
│   └── iris.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── script.js
│
└── notebooks/
    └── iris_insight.ipynb

Installation and Local Setup

Clone the repository:

git clone https://github.com/your-username/CodeAlpha_IrisInsight.git
cd CodeAlpha_IrisInsight


Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run the application:

python app.py


Open in browser:

http://127.0.0.1:5000

Deployment Notes

The application is deployed using Render

Model artifacts (.pkl files) are committed to the repository

Absolute paths are used to ensure compatibility with cloud environments

Gunicorn is configured as the production WSGI server

Real-World Applications

Automated plant species identification

Educational demonstrations of machine learning

Foundational blueprint for classification-based ML systems

Research and academic experimentation

Key Learnings

End-to-end ML project lifecycle

Model serialization and deployment

Frontend–backend integration

Cloud deployment troubleshooting

Production-ready Flask applications

Author

Sayan Mondal
Internship Project – CodeAlpha
Machine Learning & Full-Stack Development