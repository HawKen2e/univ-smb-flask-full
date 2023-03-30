from flask import Flask, request, redirect, url_for, jsonify, render_template
import json
import requests

app = Flask(__name__)
url_link_api = "http://127.0.0.1:5000"

@app.route("/")
def start(): 
    return render_template('sign_in.html')
    

@app.route("/index", methods=['POST'])
def index():
    login = request.form['login']
    passsword = request.form['password']
    donnees = list([login,passsword])
    response = requests.post(url_link_api + "/api/recevoir-donnees",json=donnees)
    if response.ok:         #print(response) -> <Response [200]>
        #ajouter la creation de la variable de session ici
        return render_template('start.html')
    else:
        return render_template('sign_in.html')

@app.route("/users")
def users():
    response = requests.get(url_link_api + "/api/user-data")
    data = response.json()
    print(data)
    return render_template('users.html', users=data)

@app.route("/list_serv_web")
def list_serv_web(): 
    return render_template('list_serv_web.html')

@app.route("/detail_conf_serv_web")
def detail_conf_serv_web(): 
    return render_template('detail_conf_serv_web.html')

@app.route("/ajout_serv_web")
def ajout_serv_web(): 
    return render_template('ajout_serv_web.html')
    
@app.route("/suppr_serv_web")
def suppr_serv_web(): 
    return render_template('suppr_serv_web.html')

@app.route("/list_serv_load_balancer")
def list_serv_load_balancer(): 
    return render_template('list_serv_load_balancer.html')

@app.route("/detail_conf_serv_load_balancer")
def detail_conf_serv_load_balancer(): 
    return render_template('detail_conf_serv_load_balancer.html')

@app.route("/ajout_serv_load_balancer")
def ajout_serv_load_balancer(): 
    return render_template('ajout_serv_load_balancer.html')
    
@app.route("/suppr_serv_load_balancer")
def suppr_serv_load_balancer(): 
    return render_template('suppr_serv_load_balancer.html')

@app.route("/list_serv_reverse_proxy")
def list_serv_reverse_proxy(): 
    return render_template('list_serv_reverse_proxy.html')

@app.route("/detail_conf_serv_reverse_proxy")
def detail_conf_serv_reverse_proxy(): 
    return render_template('detail_conf_serv_reverse_proxy.html')

@app.route("/ajout_serv_reverse_proxy")
def ajout_serv_reverse_proxy(): 
    return render_template('ajout_serv_reverse_proxy.html')
    
@app.route("/suppr_serv_reverse_proxy")
def suppr_serv_reverse_proxy(): 
    return render_template('suppr_serv_reverse_proxy.html')

@app.route("/api-test")
def api_test():
    parametre_get = request.args.get('bool')
    print(parametre_get)
    return 'true'

def check_sign_in():
    return True
