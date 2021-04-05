from flask import Flask, render_template, jsonify, request, url_for
import numpy as np
import tensorflow as tf
from tensorflow import keras
import os
from werkzeug.utils import secure_filename
from keras.preprocessing.image import load_img, img_to_array, array_to_img, save_img

# Define Flask app
app = Flask(__name__)

# Load the trained model
model = keras.models.load_model(
    '/Users/harshjhunjhunwala/Desktop/github/facial_keypoint/model.h5')


def model_predict(img_path, model):
    img = load_img(img_path, target_size=(96, 96))
    x = img_to_array(img)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/predict", methods=['GET', "POST"])
def upload():
    if request.method == "POST":
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(basepath, 'uploads',
                                secure_filename(f.filename))
        f.save(filepath)
        return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True)
