import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'id':5,
    'name':'Om Sharma',
    'roll':107,
    'city':'Parbat'
}

json_data = json.dumps(data) #changing py dict to json data

r = requests.post(url=URL,data=json_data)
data = r.json()
print(data)