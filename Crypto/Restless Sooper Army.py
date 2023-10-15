from pwn import *
from Crypto.Cipher import AES
import binascii

# connessione
HOST = "rsa.challs.olicyber.it"
PORT = 10300
r = remote(HOST, PORT)

instructions = r.recvlines(7)

# prendo in input p, q, e
val = r.recv().decode().strip().split()
print(val)
p = int(val[6])
q = int(val[13])
e = int(val[19])

# viene chiesto di mandare n
n = p * q
phi = (p-1)*(q-1)
d=pow(e,-1,phi)
r.sendline(str(n))
r.recv()
r.sendline(str(phi))
r.recv()
r.sendline(str(d))
val = r.recv().decode().strip().split()
m = val[4].strip('\'').strip(':').strip('\'')
c = pow(int(m.encode().hex(), 16), e, n)
r.sendline(str(c))
#AES
r.recvuntil('IV')
val = r.recv().decode().strip().split()
print(val)
IV = val[1]
CHIAVE = val[3]
TOKEN = bytes.fromhex(val[5])
'''
Il token è cifrato usando AES in modalità CBC,
la chiave è cifrata utilizzando RSA con gli stessi parametri visti nella challenge.'''

intCHIAVE= int(CHIAVE, 16)
chiave = pow(intCHIAVE,d,n)
chiave = chiave.to_bytes((chiave.bit_length() + 7) // 8, byteorder='big')

cipher = AES.new(chiave, AES.MODE_CBC, bytes.fromhex(IV))
decrypted_token = cipher.decrypt(TOKEN)
decrypted_token_str = decrypted_token.decode('utf-8')
print("Token decriptato:", decrypted_token_str)


r.interactive()

#flag{W3lc0m3_Ab04rD}