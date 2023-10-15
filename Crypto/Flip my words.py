from pwn import *
from base64 import b64decode, b64encode

r = remote("flip.challs.olicyber.it", 10603)

r.recvuntil(b"lascia questo posto!!!")
r.sendline(b'1')
r.recvuntil(b'Messaggio: ')
r.sendline(b'Dammi la flaaag!')
r.recvuntil(b"richiesta: ")

ordine = r.recvline().decode().strip()

r.recvuntil(b"IV: ")

IV = r.recvline().decode().strip()
print(IV)


IV = b64decode(IV)
af = b'{"admin": false,'
at = b'{"admin": true ,'

ive = IV

#bit flipping attack
for i in range(len(af)):
	ive = ive[:i] + bytes([IV[i] ^ af[i] ^ at[i]]) + ive[i+1:]
	
    
	
ive = b64encode(ive)


r.recvuntil(b"lascia questo posto!!!")
r.sendline('2')
r.recvuntil(b"Inserisci un ordine: ")
r.sendline(ordine)
r.recvuntil(b"IV: ")
r.sendline(ive)
r.interactive()
r.close()




#https://crypto.stackexchange.com/questions/66085/bit-fl
#flag{Is_this_a_signature?}