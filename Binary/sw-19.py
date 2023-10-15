from pwn import *

exe = ELF("sw-19")
r = remote("software-19.challs.olicyber.it", 13002)

instruction = r.recvlines(7)
testo = r.recv().decode().strip()
if 1==1:
    r.sendline()

while(True):
    testo = r.recv().decode().strip()
    if "flag" in testo:
        break
    testo = testo.strip("-> ").strip(":")
    resp = hex(exe.symbols[testo])
    r.sendline(resp)
print(testo)