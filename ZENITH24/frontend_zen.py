import os
import csv
from flask import Flask, render_template,request
from PIL import Image
import tensorflow as tf
from tensorflow.keras import models,layers
import numpy as np
from loading3 import *
global fp,dis
app = Flask(__name__)
@app.route("/")
def upload_image():
    return render_template("Dashboard.html")

@app.route("/predict")
def render_predict():
    return render_template("Predict.html")

@app.route("/upload_image", methods=["POST"])
def upload_file():
    global fp,dis
    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file.filename != '':
            # Get the current working directory
            current_directory = os.getcwd()
            #file_path = os.path.join(current_directory, uploaded_file.filename)
            cd1=os.path.join(current_directory,'uploads')
            cd2=os.path.join(cd1, uploaded_file.filename)
            uploaded_file.save(cd2)
            uploaded_file_path = os.path.abspath(cd2)
            fp=str(uploaded_file_path)
            print(fp)
            l=loading(fp)
            print(l)
            dis=l[0]
            #model.predict(model,fp)
            return render_template("Result.html")
    return "Error! Uploading"
@app.route("/disease")
def render_disease():
    csv_path = os.path.join(app.root_path, 'templates', 'causes.csv')
    with open(csv_path, newline='') as csvfile:
        re = csv.reader(csvfile)
        for row in re:
            if row[0]==dis:
                data=row
                print(data)
                if data!=None:
                    return render_template("Disease_Detected.html",data=data)
                else:
                    return render_template("Disease_Detected.html",data="Unfound!")
#print(render_template)
@app.route("/remedies")
def render_remedies():
    global dis
    csv_path = os.path.join(app.root_path, 'templates', 'remedies.csv')
    with open(csv_path, newline='') as csvfile:
        re = csv.reader(csvfile)
        for row in re:
            if row[0]==dis:
                data=row
                return render_template("Remedies.html",data=data)
if __name__=="__main__":
    app.run()
