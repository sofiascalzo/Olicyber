''' nc corrupted.challs.olicyber.it 10604
Abbiamo accesso al file usato per decidere i parametri crittografici su questa rete XD Puoi mettere quello che vuoi, quindi divertiti e spiali per bene!
 Sovrascrivi file con: 0 1
{"g": 0, "p": 1, "A": 0}
{"B": 0}
flag: zSgtnZ26GBEmBC8ATITRonCIva6ZETGbuZKD/Q7hTDE=
'''
'''
ho messo 1 a p in modo che mandasse tutto a 0 
in questo modo conosco gia il valore della chaive condivisa = a 0
'''

from Crypto.Cipher import AES 
from base64 import b64decode

encode = 'zSgtnZ26GBEmBC8ATITRonCIva6ZETGbuZKD/Q7hTDE='
decoded = b64decode(encode)

print(AES.new(bytes([0]*16), AES.MODE_ECB).decrypt(decoded))

#flag{usate_parametri_standard!}
