from flask import Flask, request, jsonify, render_template, session, redirect, url_for, session
import requests
import os

import pandas as pd
import numpy as np
import joblib

model_rf = joblib.load(open('model.pkl','rb'))
app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
          return render_template('index.html')
      
@app.route('/', methods = ['POST'])
def getvalue():
    taxUser = request.form['tax']
    incomeUser = request.form['income']
    highwaysUser = request.form['highways']
    licenseUser = request.form['license']
    res = model_rf.predict([[taxUser, incomeUser, highwaysUser, licenseUser]])
    return render_template('index.html', res = res)    

if __name__ =='__main__':
      port = int(os.environ.get('PORT', 3000))
      app.run(debug=True, host='0.0.0.0', port=port)
      
# add this comment to Test pushing a simple code change 