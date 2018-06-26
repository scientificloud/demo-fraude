#coding: utf-8
from flask import Flask, request, render_template, jsonify, g
import sqlite3
import base64
from config import *
app = Flask(__name__, static_url_path='/static')

DATABASE = 'database.db'

CREDENCIAIS = "c3VwZXJ1c2VyOmlyaXM="

@app.route('/receber_dados_intersystems/<int:tipo>', methods=['GET', 'POST'])
def receber_dados_intersystems(tipo):
    import requests, os, json, base64
    URL = "http://35.227.122.84:52773/api/fraud/data/form/objects/ScientifiCloud.Data.InsuranceClaim/all?size=5000&page=1&filter=statusAgent%20eq%20triage"

    headers = {
        'Authorization': 'Basic %s' %(CREDENCIAIS),
        "Content-Type": "application/json"
    }

    r = requests.get(URL, headers=headers)

    if r.status_code != 200:
        return jsonify({"Resultado": {
            "Mensagem": "Erro ao receber dados",
            "Status": False
            }
        })
    else:        
        return jsonify({"Resultado": {
            "Dados": r.json(),
            "Mensagem": "Dados recebidos com sucesso!",
            "Status": True
            }
        })


@app.route('/decisao_analista', methods=['POST', 'PUT'])
def decisao_analista():
    import requests, json
    import base64   

    dados = request.data.decode("utf-8")   
    base64json = request.args.get("base64json")
    base64json += "=" * ((4 - len(base64json) % 4) % 4)    
    json_dados = base64.b64decode(base64json)
    json_dados = json.loads(json_dados)
    json_dados = json.loads(json_dados)
    decisao = dados.replace("decisao=", "")
    json_dados.update({"trace": 0})
    json_dados['statusAgent'] = decisao

    URL = "http://35.227.122.84:52773/api/fraud/data/form/object/ScientifiCloud.Data.InsuranceClaim/" + str(json_dados["ID"])

    json_dados = json.dumps(json_dados)

    headers = {
        'Authorization': 'Basic %s' %(CREDENCIAIS),
        "Content-Type": "application/json"
    }

    r = requests.put(URL, headers=headers, data=json_dados)
    
    if(r.status_code == 200):
        return jsonify({
            "resultado":{
                "mensagem_servidor": "Dados enviados com sucesso!",
                "mensagem_intersystems": r.text,
                "status": True
            }
        })
    else:
        return jsonify({
            "resultado":{
                "mensagem_servidor": "Erro ao enviar dados!",
                "mensagem_intersystems": r.text,
                "status": False
            }
        })


@app.route('/')
def index():
   return render_template("login.html")

@app.route('/user')
def usuario():
   return render_template("index.html")

@app.route('/analyst')
def analista():
    return render_template("analista.html")


@app.route("/cadastrar_dados", methods=["GET", "POST"])
def cadastrar_dados():    
    import requests, json, base64
    URL = "http://35.227.122.84:52773/api/pmml/"
    policynumber = request.form.get("policyNumber")
    totalclaimamount = request.form.get("totalclaimamount")
    injuryclaim = request.form.get("injuryclaim")
    propertyclaim = request.form.get("propertyclaim")
    vehicleclaim = request.form.get("vehicleclaim")
    address = request.form.get("address")
    carbrand = request.form.get("carbrand")
    carplate = request.form.get("carplate")
    causador_acidente = request.form.get("causador_acidente")
    cause = request.form.get("cause")
    chassis = request.form.get("chassis")
    city = request.form.get("city")
    damage = request.form.get("damage")
    data_sinistro = request.form.get("data_sinistro")
    description = request.form.get("description")
    docnumber = request.form.get("docnumber")
    fullname = request.form.get("fullname")
    houve_vitma = request.form.get("houve_vitma")
    incidentHourOfTheDay = request.form.get("incidentHourOfTheDay")
    state = request.form.get("state")
    utilizado_seguro = request.form.get("utilizado_seguro")
    yearmodel = request.form.get("yearmodel")
    
    headers = {
        'Authorization': 'Basic %s' %(CREDENCIAIS),
        "Content-Type": "application/json"
    }

    data = {
        "policynumber": str(policynumber),
        "totalclaimamount":str(totalclaimamount),
        "injuryclaim":str(injuryclaim),
        "propertyclaim":str(propertyclaim),
        "vehicleclaim":str(vehicleclaim),
        "trace": 1,
        "yearmodel": yearmodel,
        "utilizado_seguro": utilizado_seguro,
        "state": state,
        "incidentHourOfTheDay": incidentHourOfTheDay,
        "houve_vitma": houve_vitma,
        "fullname": fullname,
        "docnumber": docnumber,
        "description": description,
        "data_sinistro": data_sinistro,
        "damage": damage,
        "city": city,
        "chassis": chassis,
        "cause": cause,
        "causador_acidente": causador_acidente,
        "carplate": carplate,
        "carbrand": carbrand,
        "address": address
    }

    r = requests.post(URL, headers=headers, data=json.dumps(data))

    r = r.json()
    if r['status'] == "fraud":       
        return jsonify({"Resultado": {
            "Modelo": {
                "Mensagem": "Irregularity has been identified, the case will be referred for audit. " + str(r['status']),
                "Resultado":str(r['reason'])
            }
        }})
    elif r['status'] == 'triage':
        return jsonify({"Resultado": {
            "Modelo": {
                "Mensagem": "This case has some inconsistencies and will be evaluated. " + str(r['status']),
                "Resultado":str(r['reason'])
            }
        }})
    elif r['status'] == 'denied':
        return jsonify({"Resultado": {
            "Modelo": {
                "Mensagem": "This case is on blacklist. " + str(r['status']),
                "Resultado":str(r['reason'])
            }
        }})
    else:
       return jsonify({"Resultado": {
            "Modelo": {
                "Mensagem": "Case ready to be sent to the payments department. " + str(r['status']),
                "Resultado":str(r['reason'])
            }
        }}) 


def get_parametros(policynumber, totalclaimamount, injuryclaim, propertyclaim, vehicleclaim):
    import requests, os, json, base64
    URL = "http://35.227.122.84:52773/api/pmml/"

    headers = {
        'Authorization': 'Basic %s' %(CREDENCIAIS),
        "Content-Type": "application/json"
    }

    data = {
        "policynumber": str(policynumber),
        "totalclaimamount":int(totalclaimamount),
        "injuryclaim":int(injuryclaim),
        "propertyclaim":int(propertyclaim),
        "vehicleclaim":int(vehicleclaim)
    }

    r = requests.post(URL, headers=headers, data=json.dumps(data))

    return r.json()


@app.route("/description")
def descricao():
    import json
    base64json = request.args.get("base64json")
    json_dados = base64.b64decode(base64json)
    json_dados = json.loads(json_dados)
    json_dados = json.loads(json_dados)

    #crio request de dados
    parametros = get_parametros(json_dados['policyNumber'],json_dados['totalClaimAmount'],json_dados['injuryClaim'],json_dados['propertyClaim'],json_dados['vehicleClaim'])
    
    return render_template("descricao.html", dados=json_dados, modelo=parametros)

if __name__ == "__main__":
    app.run(host=servidor['host'], debug=servidor['debug'], port=servidor['porta'])