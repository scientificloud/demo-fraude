#Esse script é apenas para testes.
#Desconsiderar.

import requests, os, json, base64
URL = "http://35.227.122.84:52773/api/fraud/data/form/objects/ScientifiCloud.Data.InsuranceClaim/216738"
#credenciais = b64encode(b"superuser:123").decode("ascii")

credenciais = base64.b64encode("superuser:iris".encode("utf-8"))
credenciais = str(credenciais).split("'")[1]
headers = {
    'Authorization': 'Basic %s' %(credenciais),
    "Content-Type": "application/json"
}

r = requests.post(URL, headers=headers)


print(r.status_code)
print(r.text)