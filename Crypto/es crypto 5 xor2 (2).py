def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

ciphertext = bytes.fromhex('104e137f425954137f74107f525511457f5468134d7f146c4c')

for k in range(256):
    m = (xor(ciphertext, bytes([k]*len(ciphertext))))
    if b'-' in m:
        print(m)
