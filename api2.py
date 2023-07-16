# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 14:39:00 2023

@author: User
"""

from flask import Flask

app = Flask(__name__)

allgoods = [
    
    {
     "id":5,
     "name":"王品牛排吃到飽",
     "price":550
     },
    {
     "id":6,
     "name":"吹到冷冷氣機",
     "price":45050
     }
    
    ]

@app.route("/getGoods")
def Agoods():
    return {"goods":{"starus":"success","product":allgoods}},200

if __name__ == "__main__":
    app.run(port=5566,debug=True)