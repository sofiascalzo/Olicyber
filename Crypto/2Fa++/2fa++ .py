from Crypto.Cipher import AES
from hashlib import sha256
from pwn import *

MAXN = 1_000_000
passphrase = b'\x00'*16

def expand_pin(pin):
    return sha256(pin).digest()[:16]

expd = {}
enc = [(0, 0)]*MAXN
payload = ''
for x in range(MAXN):
    if x % 100000 == 0: print(x)
    expd[x] = expand_pin(str(x).zfill(6).encode())
    c1 = AES.new(expd[x] , AES.MODE_ECB)
    val = c1.decrypt(passphrase)
    enc[x] = (val, x)
    payload += val.hex()
enc.sort()
print("finish")


def fast_index(value):
    l = 0 
    r = len(enc)-1
    while l <= r:
        mid = (l+r) >> 1
        if enc[mid][0] == value:
            return enc[mid][1]
        elif enc[mid][0] < value:
            l = mid+1
        else:
            r = mid-1
    return -1

con = remote('2fapp.challs.olicyber.it',12207)
con.recvlines(8)
con.sendline(b'3')
con.recvuntil(b': ')
con.sendline(b'admin')
con.recvuntil(b': ')
con.sendline(payload.encode())
con.recvuntil(b': ')
encd = con.recvline().decode()[:-1]
encd = bytes.fromhex(encd)

print("done")
found1 = 0
found2 = 0
for pin1 in range(MAXN):
    if pin1 % 100000 == 0: print(pin1)
    c1 = AES.new(expd[pin1], AES.MODE_ECB)
    block = encd[pin1*16:pin1*16+16]
    bo = c1.decrypt(block)

    pin2 = fast_index(bo)
    if pin2 > 0:
        print(pin1, pin2)
        found1,found2 = pin1, pin2

con.recvlines(8)
con.sendline(b'2')
con.recvuntil(b': ')
con.sendline(b'admin')
con.recvuntil(b': ')
con.sendline(str(found1).encode())
con.recvuntil(b': ')
con.sendline(str(found2).encode())
con.interactive()
