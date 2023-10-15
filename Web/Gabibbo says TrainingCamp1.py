import requests 
url = "http://gabibbo-says.challs.olicyber.it/"
#data = {"username": "admin", "password": "admin"}
data = {"gabibbo": "angry"}
res = requests.post(url, data=data)
print(res.headers) 
print(res.text)




