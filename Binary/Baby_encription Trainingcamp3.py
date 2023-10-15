'''
per vedere il valore delle variabili su ghidra, clicco sul nome della variabile in viola
nella finestra accanto il decompiler, e poi clicco sulla vsualizza bytes dove mi fa vedere da dove inizia
'''
target = b"\x27\x2d\x20\x26\x3a\x36\x29\x70\x2d\x72\x70\x1e\x39\x71\x33\x3c"
key = b"\xf8\x6f\x86\x83\xc3\x9c\x8b\x35\xf0\xc0\x87\x92\x2e\x41\x2b\x53"

def rotate_key(key):
    return key[-1:] + key[:-1]

for i in range(16):
    target = bytes([target[j] ^ key[j] for j in range(len(target))])
    key = rotate_key(key)

flag = target.decode()
print(flag)

#flag{wh1l31_x0r}