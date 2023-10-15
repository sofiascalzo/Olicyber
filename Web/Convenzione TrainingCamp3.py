import requests
import os

URL = os.environ.get('URL', 'http://convenzione.challs.olicyber.it/')
res = requests.request('FLAG', URL)
print(res.headers)
