from Crypto.Cipher import DES, AES, ChaCha20
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# DES
key = bytes.fromhex('ff074f1e92c926ff')
cipher = DES.new(key, DES.MODE_CBC)
plaintext = 'La lunghezza di questa frase non è divisibile per 8'

# print(len(plaintext))

padded = pad(plaintext.encode(), 8, 'x923')
# print(len(padded))
 
ciphertext = cipher.encrypt(padded)
print(ciphertext.hex())
print(cipher.iv.hex())
print('------------------------------')

# AES
key = get_random_bytes(32)
print(key.hex())
# key = bytes.fromhex('770a5395ce6d0f6a585600290bf53510ac430349a90aaa198b1b7b1bb8512bc2')
cipher = AES.new(key, AES.MODE_CFB, segment_size = 24)
plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
padded = pad(plaintext.encode(), 16, 'pkcs7')
ciphertext = cipher.encrypt(padded)
print(ciphertext.hex())
print(cipher.iv.hex())
print('------------------------------')

# ChaCha20
key = bytes.fromhex('4356147f2610b51adbb2507a508451fa21a4cdb114a24293b01b1568cf5bf895')
nonce = bytes.fromhex('e7ceeee98c570786')
cipher = ChaCha20.new(key=key, nonce=nonce)
ciphertext = bytes.fromhex('ea5a47e7e57730ffe75e949cce9a9a7eec28ccb2dd86b63cb32bda9e')
plaintext = cipher.decrypt(ciphertext)
print(plaintext.decode())
print(plaintext)