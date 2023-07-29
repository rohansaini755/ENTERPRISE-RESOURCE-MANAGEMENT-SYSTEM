from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import cv2
import keras
import errno
from waitress import serve
import requests
import json



# Keras
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template, request, jsonify
#from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from flask_cors import CORS
from flask import jsonify,send_from_directory

app = Flask(__name__)
# MODEL_PATH = 'models/model.h5'

# Load your trained model
# model = keras.models.load_model(MODEL_PATH)

# model = keras.models.load_model(MODEL_PATH)

#model._make_predict_function()      
print('Model loaded. Start serving...')

print('Model loaded. Check http://127.0.0.1:5000/')



def model_predict(img_path, model):
    
    #update by ViPS
    img = cv2.imread(img_path)
    new_arr = cv2.resize(img,(256,256))
    new_arr = np.array(new_arr/255)
    new_arr = new_arr.reshape(-1, 256, 256, 3)
    

    
    preds = model.predict(new_arr)
    return preds


CORS(app, origins='*')

# Load your trained model
# model = keras.models.load_model('models/model.h5')

@app.route('/company_detail_page/<path:filename>', methods=['GET'])
def get_image(filename):
    return send_from_directory('static', filename)

@app.route('/aso_company', methods=['GET'])
def aso_company():
    return render_template('associated_company.html')


@app.route('/templates/<id>', methods=['GET'])
def templates(id):
    parsed_data = {}
    parsed_data['id'] = id
    return render_template('templates.html',data=parsed_data)

@app.route('/company_product/<id>', methods=['GET'])
def company_product(id):
    print(id)
    response = requests.post('http://127.0.0.1:8000/company_detail_v/', json={'id': id})
    if response.status_code == 200:
        data = response.json()
        json_data = data['data']
        parsed_data = json.loads(json_data)
        print(type(parsed_data))
        print(parsed_data)
        return render_template('company_product.html', data=parsed_data)
    else:
        return "Error: Failed to fetch company details."

@app.route('/new_company', methods=['GET'])
def new_company_form():
    return render_template('new_company_form.html')

@app.route('/login_page',methods=['GET','POST'])
def login_page():
    return render_template('login.html')

@app.route('/branch_profile/<id>',methods=['GET'])
def branch_profile(id):
    response = requests.post('http://127.0.0.1:8000/branch-profile/',josn={'id':id})
    if response.status_code == 200:
        data = response.josn()
        j_data = data['data']
        parsed_data = json.loads(j_data)
        return render_template('branch-profile.html',data=parsed_data)
    else:
        return "error: failed to fetch branch detail."

@app.route('/farmer_profile/<id>',methods=['GET'])
def farmer_profile(id):
    response = requests.post('http://127.0.0.1:8000/farmer_detail/',json={'id':id})
    if response.status_code == 200:
        data = response.json()
        json_data = data['data']
        parsed_data = json.loads(json_data)
        print(type(parsed_data))
        print(parsed_data)
        return render_template('farmer_page.html',data=parsed_data)
    else:
        print("data not found")
        return "error: failed to fetch farmer detail."

@app.route('/company_detail_page/<id>',methods=['GET'])
def company_detail_page(id):
    response = requests.post('http://127.0.0.1:8000/company_detail_v/', json={'id': id})
    if response.status_code == 200:
        data = response.json()
        json_data = data['data']
        parsed_data = json.loads(json_data)
        print(type(parsed_data))
        print(parsed_data)
        return render_template('company_detail_page.html', data=parsed_data)
    else:
        return "Error: Failed to fetch company details."


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/home',methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/dashboard',methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/farmer',methods=['GET'])
def farmer():
    return render_template('farmer_page.html')

@app.route('/branches',methods=['GET'])
def branches():
    return render_template('branches_list.html')

@app.route('/history',methods = ['GET'])
def history():
    return render_template('history.html')

@app.route('/product_list/<id>',methods=['GET'])
def product_list(id):
    data = {}
    data['id'] = id
    # json_data = json.loads(data)
    return render_template('product_list.html',data=data)

@app.route('/new',methods=['GET'])
def new_farmer():
    return render_template('new_farmer_form.html')

# Rest of your route handlers...

# @app.route('/predict', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#     # Get the file from post request
#         f = request.files['file']

#         # Save the file to ./uploads
#         basepath = os.path.dirname(__file__)
#         file_path = os.path.join(
#             basepath, 'uploads',f.filename )  #secure_filename(f.filename)
#         f.save(file_path)

#         # Make prediction
#         preds = model_predict(file_path, model)

#         # Process your result for human
#         pred_class = preds.argmax()              # Simple argmax

        
#         CATEGORIES = ['Pepper__bell___Bacterial_spot','Pepper__bell___healthy',
#             'Potato___Early_blight' ,'Potato___Late_blight', 'Potato___healthy',
#             'Tomato_Bacterial_spot' ,'Tomato_Early_blight', 'Tomato_Late_blight',
#             'Tomato_Leaf_Mold' ,'Tomato_Septoria_leaf_spot',
#             'Tomato_Spider_mites_Two_spotted_spider_mite' ,'Tomato__Target_Spot',
#             'Tomato__YellowLeaf__Curl_Virus', 'Tomato_mosaic_virus',
#             'Tomato_healthy']
#         return CATEGORIES[pred_class]

#         #return CATEGORIES[pred_class]
#     return None






app = Flask(__name__, static_url_path='/static')

if __name__ == '__main__':
    app.run(debug =True)

