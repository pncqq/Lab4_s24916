import requests
import json

url = 'http://127.0.0.1:5000/predict'

data = {
    "features": [-1.21388,0.13288,-0.74027,0.83021,0.11071,2.23148,-0.48129,-0.90890,-0.50404,-0.39381,0.47630,-0.55063,-1.61145,-0.50527,-0.72657,0.82038,-1.32694,-0.61237,0.04556]
}

headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)

print("Parsed response:", response.json())
