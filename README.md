## Movie Genre Classification Web App

This project is a simple web application built with Flask, HTML, CSS, and scikit-learn for classifying the genre of a movie plot. The app uses a Support Vector Classifier (SVC) model trained on TF-IDF vectorized movie plots.

### How to Run the Project

Follow the steps below to run the project:

#### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

git clone <repository-url>

#### Step 2: Set up Environment

Create a virtual environment using conda. Run the following command to create a new environment with Python 3.9:

'''conda create -p venv python=3.9 -y'''

Activate the virtual environment:

'''conda activate venv'''


#### Step 3: Install Dependencies

Install the required packages by running the following command:
'''pip install -r requirements.txt'''

#### Step 4: Install IPython Kernel

'''pip install ipykernel'''

Step 5: Run the Flask App
Run the Flask app by executing the app.py file:

'''python app.py'''


The app should now be running locally on `http://127.0.0.1:5000/`. Open this URL in your web browser to use the movie genre classification web app.

### Usage

1. Enter the plot of a movie in the provided text area.
2. Click the "Predict Genre" button to classify the genre of the movie plot.
3. The predicted genre will be displayed on the same page.

