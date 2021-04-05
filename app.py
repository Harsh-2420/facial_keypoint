from flask import Flask, render_template, jsonify, request
import numpy as np
import tensorflow as tf
from tensorflow import keras

app = Flask(__name__)
model = keras.models.load_model(
    '/Users/harshjhunjhunwala/Desktop/github/facial_keypoint/model.h5')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/uploader", methods=["POST"])
def upload_file():
    if request.method == "POST":
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'


# @app.route("/predict", methods=["POST"])
# def predict():
#     int_features = [int(x) for x in request.form.values()]


if __name__ == '__main__':
    app.run(debug=True)
