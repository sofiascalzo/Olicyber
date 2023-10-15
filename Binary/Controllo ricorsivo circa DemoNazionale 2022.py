'''
from pwn import *

r=remote("crc.challs.olicyber.it",12201)
print(r.recv())

def calculate_crc16(data):
    crc = 0xFFFF 

    for byte in data:
        crc ^= byte  

        for _ in range(8):
            if crc & 0x0001:
                crc >>= 1
                crc ^= 0xA001 
            else:
                crc >>= 1

    return crc

target_crc = -8101

value_to_check = 0
while True:
    crc_result = calculate_crc16(value_to_check.to_bytes(2, byteorder='big', signed=True))
    if crc_result == target_crc:
        break
    value_to_check += 1

print(r.sendline((str(found_value).encode())))

r.interactive()
'''

from pwn import *

file = open("rockyou.txt", "r")

for i in file:
    r=remote("crc.challs.olicyber.it", 12201)
    r.recv()
    r.sendline(i.encode())
    flag=r.recv()

    print(i+"\n")
    print(flag)

#flag{not_crypto_secure_hash_53cd8ab4e}
#sweets