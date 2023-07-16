# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 14:31:15 2023

@author: User
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello LCC"

if __name__=="__main__":
    app.run(port=5566,debug=True)