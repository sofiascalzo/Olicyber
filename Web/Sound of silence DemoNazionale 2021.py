import requests

url = "http://soundofsilence.challs.olicyber.it/"
data = {"input[]": ""}

response = requests.post(url, data=data)

if response.status_code == 200:
    print(response.text)
else:
    print("Errore")
