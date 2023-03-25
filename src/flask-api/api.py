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
    donnees = request.json
    send_slq_pw_user(donnees)
    return 'je vien de api.py'

def send_slq_pw_user(donnees):
    login =[]
    login.insert(0, donnees[0])
    #login = donnees[0]
    pw = donnees[1]
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM user_pw WHERE login_pw = %s", (login))
    rows = cursor.fetchall()
    print(rows)
    result = []
    for row in rows:
        result.append({'login_pw': row[0], 'password': row[1]})
    if (result[0]['password'] == pw) :
        return True
    else :
        return False
   

#print(type(mydb))