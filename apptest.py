from __future__ import division
from math import sqrt
from flask import Flask, render_template, request, jsonify, url_for
from collections import Counter
from flask import Flask, request
from predict import Predictor
from model import Model
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

M = Model()
predictor = Predictor()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict/<text>')
def predict(text):
    prediction =  predictor.predict([text])
    return jsonify(prediction)

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run(host='your local host ip')
