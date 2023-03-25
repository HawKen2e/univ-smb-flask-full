from flask import Flask, request
import json
import mysql.connector
from db import mydb

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, API!"


@app.route('/api/recevoir-donnees', methods=['POST'])
def recevoir_donnees():
    print('ca passe')
    return 'je vien de api.py'

print(type(mydb))