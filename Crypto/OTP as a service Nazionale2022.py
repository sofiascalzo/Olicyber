from pwn import remote
import time
import random

#usando la connessione da remoto, l orario di quando cripto
#è lo stesso di quando decripto, pertanto conoscendo il seme
#è possibile generare lo stesso r e quindi invertire le operazioni

r = remote("otp1.challs.olicyber.it", 12304)
t = int(time.time())
random.seed(t)
r.recvlines(4)
r.sendline("e")
data = r.recvline(False).decode()
data = list(map(int, data.split("-")))

flag = []
for c in data:
    rnd = random.randint(0, 255)
    m = (c-rnd) % 256
    flag.append(m)
print(bytes(flag))

