ciphflag = "d45cdcbb6b1ed34a4a5ed2dfac7c"
key = "b230bddc107ae17b2c3be2ec9901"

ciphflag = bytes.fromhex(ciphflag)
key = bytes.fromhex(key)

def xor(ciphflag, key):
    return bytes([x^y for x,y in zip(ciphflag,key)])


print(xor(ciphflag,key))
