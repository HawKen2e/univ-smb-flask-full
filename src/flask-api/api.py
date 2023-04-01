from flask import Flask, request, redirect, url_for, jsonify
import json
import mysql.connector
from db import mydb

app = Flask(__name__)

url_link_website = "http://127.0.0.1:5001"

@app.route("/")
def hello():
    return "Hello, API!"


@app.route('/api/recevoir-donnees', methods=['POST'])
def recevoir_donnees():
    donnees = request.json
    if (send_slq_pw_user(donnees)):
        return 'je vien de api.py'

@app.route('/api/user-data', methods=['GET'])
def donnee_utilisateur():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM user ORDER BY login")
    rows = cursor.fetchall()
    users = []
    for row in rows:
        user = ({'login': row[0], 'first_name': row[1], 'last_name': row[2]})
        users.append(user)
    return jsonify(users)

@app.route('/api/recevoir-donnees', methods=['POST'])
def recevoir_donnees():
    donnees = request.json
    if (send_slq_pw_user(donnees)):
        return 'je vien de api.py'

def send_user_datas():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM user ORDER BY login")
    rows = cursor.fetchall()
    users = []
    for row in rows:
        user = ({'login': row[0], 'first_name': row[1], 'last_name': row[2]})
        users.append(user)
    print(users)
    return jsonify(users)


def send_slq_pw_user(donnees):
    login = []
    login.insert(0, donnees[0])
    pw = donnees[1]
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM user_pw WHERE login_pw = %s", (login))
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append({'login_pw': row[0], 'password': row[1]})
    if (result[0]['password'] == pw) :
        bool_param = True
    else :
        bool_param = False
    return bool_param

   

#print(type(mydb))