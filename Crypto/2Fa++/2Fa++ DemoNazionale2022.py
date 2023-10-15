from pwn import *
from Crypto.Cipher import AES
from hashlib import sha256
from binascii import unhexlify
import time

start_time = time.time()




#devo mandare 10^6 (provandoli tutti) in modo che uno di questi semplifichi la prima operazione (ek1(dk2(ek1)))
#per questioni di tempo devo fare tutto in uno stesso testo formato da 10^6 blocchi ognuno decifrato con un k1 diverso
#questo lo posso fare perchè si tratta di aes ecb quindi ogni blocco è indipendente dall'altro


def expand_pin(pin):
    return sha256(pin).digest()[:16]

start_pin = 0
num_pins = 10**6   #provo tutte le possibili k1
passphrase = b"gabibbo_hates_me"


print("sto creando il payload...")
payload = ""

for pin in range(num_pins):
    pin = str(pin).zfill(6).encode()
    c1 = AES.new(expand_pin(pin), AES.MODE_ECB)
    hashed_result = c1.decrypt(passphrase).hex()
    payload += hashed_result
    
'''
with open("plaintextmalevolo.txt", "w") as file:
    file.write(payload)
print("file creato")


with open("plaintextmalevolo.txt", "r") as file:
    payload = file.read()
'''

r=remote("2fapp.challs.olicyber.it", 12207)

benv=r.recvuntil(b'Esci')
print(benv)
r.sendline(b"3")
r.recv()
r.sendline(b"admin")
r.recv()
r.sendline(payload)
print("sto calcolando il token...")
token=r.recvline().strip().split(b':')[2].decode()
#print(token)


#ora ho il token immenso e in uno di questi casi sono nella situazione di prima quindi applico mitm
token_bytes = bytearray.fromhex(token)
token_bytes = [token_bytes[i:i+16] for i in range(0, len(token_bytes), 16)]
print("sto cercando i pin...")

s = {}
for i in range(10**6):
    pin1 = str(i).zfill(6).encode()
    c1 = AES.new(expand_pin(pin1), AES.MODE_ECB)
    s[c1.decrypt(token_bytes[i % len(token_bytes)])] = pin1


for i in range(10**6):
    pin2 = str(i).zfill(6).encode()
    c2 = AES.new(expand_pin(pin2), AES.MODE_ECB)
    decrypted_passphrase = c2.decrypt(passphrase)
        

    if decrypted_passphrase[:16] in s:
        pin1 = s[decrypted_passphrase[:16]]
        break

print("trovati")
end_time = time.time()
elapsed_time = end_time - start_time
minutes = int((elapsed_time % 3600) // 60)
seconds = int(elapsed_time % 60)
print(f"Tempo trascorso: {minutes} minuti, {seconds} secondi")

#login
benv=r.recvuntil(b'Esci')
r.sendline(b'2')
r.recv()
r.sendline(b"admin")
r.recv()
r.sendline(str(pin1).encode())
r.recv()
r.sendline(str(pin2).encode())
r.interactive()
#flag=r.recvline(False).decode()
#print(flag)



#flag{m337_1n_7h3_m1ddl3_57r1k35_b4ck}         #Tempo trascorso: 3 minuti, 47 secondi
#https://crypto.stackexchange.com/questions/88411/triple-aes-128-encryption-with-2-key2