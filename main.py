#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:17:42 2020

@author: amberchen
"""

from flask import Flask, render_template, request
from compare import * 
app = Flask(__name__)
@app.route('/')
def input():
   return render_template('input.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      #print(result)
      score=calculate_score(result)
      result=dict(result)
      result['Score']=score
      #print(score)
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True,host='0.0.0.0')