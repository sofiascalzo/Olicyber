from pwn import *

HOST = "software-17.challs.olicyber.it"
PORT = 13000

r = remote(HOST, PORT)
instructions = r.recvlines(6)
testo = ""

testo = r.recv().decode().strip()
if 1==1:
    r.sendline()

for i in range(10):
    somma = 0
    testo = r.recvline().decode().strip()
    testo = r.recvline().decode().strip().strip('[').strip(']')      
    num = testo.split(", ")
    for Armando in num:
        somma += int(Armando)
    r.recv()
    print("somma: ", somma)
    r.sendline(str(somma))
    
flag = r.recv().decode().strip()
print(flag)