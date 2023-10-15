from pwn import *

#connessione
HOST = "software-18.challs.olicyber.it"
PORT = 13001
r = remote(HOST, PORT)

#invio un carattere
instructions = r.recvlines(7)
test = r.recv()
if 1==1:
    r.sendline()

#ciclo for
for i in range(100):
    print(f"Solving test n.{i+1}..", end=" ")
    test = r.recvline().decode().strip()
    op = test.split()

    num = int(op[5], 16)

    #codifica in base64 o base32
    if op[8] == "64-bit":
        res = p64(num)
    elif op[8] == "32-bit":
        res = p32(num)
    else:
        print(test)
    print("Done")

    #stampo il risultato
    r.recv()
    r.send(res)

#riscatto la flag
flag = r.recv().decode()
print(flag)