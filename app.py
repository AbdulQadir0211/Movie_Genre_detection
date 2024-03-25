from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)


# Load the pre-trained model and vectorizer
tfidf_vectorizer = joblib.load("model/tfidf_vectorizer.pkl")
model = joblib.load("model/model.pkl")
le = joblib.load("model/label_encoder.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    plot_text = request.form['plot']
    plot_tfidf = tfidf_vectorizer.transform([plot_text])
    genre_encoded = model.predict(plot_tfidf)
    predicted_genre = le.inverse_transform(genre_encoded)[0]
    return render_template('index.html', predicted_genre=predicted_genre, plot_text=plot_text)

if __name__ == '__main__':
    app.run(debug=True)