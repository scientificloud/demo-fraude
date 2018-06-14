#coding: utf-8
from flask import Flask, request, render_template, jsonify, g
import sqlite3
import base64
app = Flask(__name__, static_url_path='/static')

DATABASE = 'database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    try:
        cur = get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv
    except Exception as e:
        print("Sem erros")
        print(e)
        pass

def insert(query, args):
    # g.db is the database connection
    cur = get_db()  
    cur.execute(query, args)
    get_db().commit()
    cur.close()


@app.route('/receber_dados_intersystems/<int:tipo>', methods=['GET', 'POST'])
def receber_dados_intersystems(tipo):
    import requests, os, json, base64
    URL = "http://35.227.122.84:52773/api/fraud/data/form/objects/ScientifiCloud.Data.InsuranceClaim/all"

    credenciais = base64.b64encode("superuser:iris".encode("utf-8"))
    credenciais = str(credenciais).split("'")[1]

    headers = {
        'Authorization': 'Basic %s' %(credenciais),
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


@app.route('/decisao_analista', methods=['POST'])
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

    json_dados['statusAgent'] = decisao   


    URL = "http://35.227.122.84:52773/api/fraud/data/form/object/ScientifiCloud.Data.InsuranceClaim/" + json_dados["ID"]

    credenciais = base64.b64encode("superuser:iris".encode("utf-8"))
    credenciais = str(credenciais).split("'")[1]
    headers = {
        'Authorization': 'Basic %s' %(credenciais),
        "Content-Type": "application/json"
    }
    
    r = requests.post(URL, headers=headers, data=json.dumps(json_dados))
    
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

@app.route('/usuario')
def usuario():
   return render_template("index.html")

@app.route('/analista')
def analista():
    return render_template("analista.html")


@app.route("/cadastrar_dados", methods=["GET", "POST"])
def cadastrar_dados():    
    import requests, json, base64
    URL = "http://35.227.122.84:52773/api/pmml/"
    policynumber = request.form.get("numero_apolice")
    totalclaimamount = request.form.get("totalclaimamount")
    injuryclaim = request.form.get("injuryclaim")
    propertyclaim = request.form.get("propertyclaim")
    vehicleclaim = request.form.get("vehicleclaim")




















    
    credenciais = base64.b64encode("superuser:iris".encode("utf-8"))
    credenciais = str(credenciais).split("'")[1]
    headers = {
        'Authorization': 'Basic %s' %(credenciais),
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

    r = r.json()
    if r['status'] == "fraud":       
        return jsonify({"Resultado": {
            "Modelo": {
                "Mensagem": "Fraude detectada.",
                "Resultado":str(r['reason'])
            }
        }})
    elif r['status'] == 'triage':
        return jsonify({"Resultado": {
            "Modelo": {
                "Mensagem": "Caso movido para triagem",
                "Resultado":str(r['reason'])
            }
        }})
    else:
       return jsonify({"Resultado": {
            "Modelo": {
                "Mensagem": "O caso não é fraude.",
                "Resultado":str(r['reason'])
            }
        }}) 


def get_parametros(policynumber, totalclaimamount, injuryclaim, propertyclaim, vehicleclaim):
    import requests, os, json, base64
    URL = "http://35.227.122.84:52773/api/pmml/"

    #credenciais = b64encode(b"superuser:123").decode("ascii")

    credenciais = base64.b64encode("superuser:iris".encode("utf-8"))
    credenciais = str(credenciais).split("'")[1]
    headers = {
        'Authorization': 'Basic %s' %(credenciais),
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


@app.route("/descricao")
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
    app.run(debug=False, host='0.0.0.0', port=8080)


# create_table_sql = """CREATE TABLE IF NOT EXISTS sinistros(
#                 id INTEGER PRIMARY KEY,
#                 anomodelo_veiculo text,
#                 causa_sinistro text,
#                 chassi_veiculo text,
#                 cidade_sinistro text,
#                 danos_sinistro text, 
#                 data_sinistro text,
#                 descricao_sinistro text,
#                 doc_segurado text,
#                 endereco_sinistro text, 
#                 estado_sinistro text, 
#                 hora_sinistro text, 
#                 marca_veiculo text,
#                 nome_segurado text, 
#                 numero_apolice text,
#                 placa_veiculo text,
#                 status text,
#                 sla real,
#                 score real
#             )"""
# conn = sqlite3.connect(DATABASE)
# conn.execute(create_table_sql)
# conn.close()