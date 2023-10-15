from pwn import *
import hashlib

HOST = 'rabbit.challs.olicyber.it'
PORT = 10501
r = remote(HOST, PORT) 

r.recvuntil(b'Execute:')
target = r.recv().decode().strip().split()[2]
print(target)

i = 0
while True:
    h = hashlib.sha1(str(i).encode('ascii')).hexdigest()
    if h.endswith(target):
        r.sendline(str(i).encode())
        break

    i += 1
    
r.interactive()

#cat * | grep flag
# flag{....c0mpl3x_And_4m4.....}

#env
#FLAG=flag{l1nux_15_4_.....}

#cd var
#cd log
#cat flg
#flag{......Z1ng_cr34Tur3}

#flag{l1nux_15_4_c0mpl3x_And_4m4Z1ng_cr34Tur3}

