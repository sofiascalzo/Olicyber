from Crypto.Cipher import AES
from Crypto.Random.random import randint
from hashlib import sha256
from pwn import *

r=remote('2fa.challs.olicyber.it',12206)
benv=r.recvuntil(b'Esci')
r.sendline(b'3') #utenti registrati
r.recvuntil(b'admin')
token=r.recvline().strip()
token=token.split(b':')[1].decode()
print(token)
#btoken=bytes.fromhex(token)



#meet in the middle attack

def expand_pin(pin):
    return sha256(pin).digest()[:16]

passphrase = b"donttrustgabibbo"

btoken = bytes.fromhex(token)

print("sto cercando i pin...")
s = {}
for i in range(10**6):
    pin1 = str(i).zfill(6).encode()
    c1 = AES.new(expand_pin(pin1), AES.MODE_ECB)
    s[c1.decrypt(btoken)] = pin1


for i in range(10**6):
    pin2 = str(i).zfill(6).encode()
    c2 = AES.new(expand_pin(pin2), AES.MODE_ECB)
    if c2.encrypt(passphrase) in s:
        #print("TROVATO!")
        #print(pin2)
        pin1 = s[c2.encrypt(passphrase)]
        #print(pin1)
        break

print("pin trovati")
benv2=r.recvuntil(b'Esci')
print(benv2)
r.sendline(b'2')          #login
r.recvuntil(b'Username:')
r.sendline(b'admin')
r.recvuntil(b'personale:')
r.sendline(pin1)
r.recvuntil(b'server:')
r.sendline(pin2)
flag=r.recvline(False).decode()
print(flag)
r.interactive()
r.close()

#flag{f0r53_d0vr31_r1v3d3r3_1l_516n1f1c470_d1_4u73n71c4z10n3_4_2_f4770r1}