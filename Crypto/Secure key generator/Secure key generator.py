from hashlib import sha256
from datetime import datetime
import random

def xor_with_key(block, key):
    return [k ^ b for k, b in zip(key, block)]

def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes(xbytes):
    return int.from_bytes(xbytes, 'big')

def generate_secure_key():
    """
    per la generazione della chiave viene usata una data
    che troviamo come commento della challenge (2021-03-21 17:37:40)
    """
    # 2021-03-21 17:37:40
    ts = int(datetime.timestamp(datetime(2021, 3, 21, 17, 37, 40))) # 1616344660
    h = sha256(int_to_bytes(ts)).digest()

    seed = int_from_bytes(h[32:])
    key = h[:32]
    
    random.seed(seed)
    for _ in range(32):
        key += bytes([random.randint(0, 255)])

    return key

"""
ho copiato e incollato il codice della challenge
per generare la medesima chiave usata per cifrare il file flag.enc
"""
key = generate_secure_key()
print('key =', key.hex())

with open("flag.enc", "rb") as f:
    stream = f.read()

ans = b""
for x in range(len(stream)):
    ans += bytes([key[x % 64] ^ stream[x]])

print(ans[:20])
with open("flag.pdf", "wb") as fa:
   fa.write(ans)



# Oppure carica su CyberChef il file flag.enc e usa come chiave la stringa generata. Uscirà un pdf con la flag
# flag{doh_these_programmers_xD_}
