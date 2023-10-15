import requests
import json

url = 'http://web-09.challs.olicyber.it/login'

data = {
    'username': 'admin',
    'password': 'admin'
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, data=json.dumps(data), headers=headers)

flag = response.text.strip()
print(f"Flag: {flag}")
