from flask import Flask, render_template, jsonify, request
import numpy as np
import tensorflow as tf
from tensorflow import keras

app = Flask(__name__)
model = keras.models.load_model(
    '/Users/harshjhunjhunwala/Desktop/github/facial_keypoint/model.h5')

# @app.route("/")
# def home():
#     return
