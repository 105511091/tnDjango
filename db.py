# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 09:55:24 2023

@author: User
"""

import mysql.connector

conn = mysql.connector.connect(host='127.0.0.1',user='tngood',password='987654321',database='tndjango',auth_plugin='mysql_native_password')

cursor = conn.cursor()