from pwn import xor

init = b"\xf3\x0f\x1e\xfa\x48\x83\xec\x08\x48\x8b\x05\xd9\x2f\x00\x00\x48\x85\xc0\x74\x02\xff\xd0\x48\x83\xc4\x08\xc3"
str=b"\x95\x63\x7f\x9d\x33\xb2\xd9\x57\x3c\xe3\x34\xec\x70\x63\x30\x2c\xb6\x9f\x44\x70\xa0\xbe\x78\xf7\xb9\0"

flag=xor(init,str)
print(flag)

#flag{15_th15_c0d3_0r_n0t}