#Enterprise Encryption

c = bytes.fromhex("7971737c7e6d7866646f2c28712e7c2f2f717b402e2b7177292b40772e402a73402f71732f402867407b2c62")

key = 31
encrypted = bytes([x ^ key for x in c])

for i in range(len(encrypted)):
    if i % 2 == 0:
        print(chr(encrypted[i]), end='')
        
for i in range(len(encrypted)):
    if i % 2 == 1:
        print(chr(encrypted[i]), end='')
