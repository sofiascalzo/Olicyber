import math
from pwn import *
r=remote("nt-master.challs.olicyber.it", 11001)
r.recvlines(4)

def find_numbers_with_sum(N):
    for a in range(1, N // 2 + 1):
        b = N - a
        gcd_ab = math.gcd(a, b)
        if gcd_ab != 0 and gcd_ab + (a * b) // gcd_ab == N:
            return a, b
    return None

for i in range (10):
    N=int(r.recvline().split()[-1].decode())
    print(N)

    a, b = find_numbers_with_sum(N)
    if a > b:
        r.send(str(a).encode())
        r.send(b" ")
        r.sendline(str(b).encode())
    else:
        c=a
        a=b
        b=c
        r.send(str(a).encode())
        r.send(b" ")
        r.sendline(str(b).encode())
    print(r.recvline())
    
r.interactive()

#ptm{as_dumb_as_a_sanity_check_4976ab37ed7f66e}