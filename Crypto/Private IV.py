'''
How encryption works:
C0= Ek(IV^P0)
C1= Ek(C0^P1)
C2= Ek(C1^P2)

The attacker can now modify the ciphertext as following:
C0'=C0; C1'=0; C2'=C0

And pass it to the decryption oracle, which will indeed return

P0=IV^DK(C0')
P1=C0'^DK(0)
P2=0^DK(C0')

P0^P2=IV^Dk(C0')^DK(C0')=IV=Key
'''


'''
Inserisci il messaggio: 
101010101010101010101010101010100000000000000000000000000000000010101010101010101010101010101010
Il messaggio decriptato è: 7378ab6d23940bb2dfb7f631150bc5bd446833f4d9b6e6884aafba9164f5622e1514ca0a58b53e81bcc5c5454a62b3c0
'''


'''
P0=7378ab6d23940bb2dfb7f631150bc5bd
P1=446833f4d9b6e6884aafba9164f5622e
P2=1514ca0a58b53e81bcc5c5454a62b3c0

P0^P2
'''


def hex_xor(hex_str1, hex_str2):
    xor_result = int(hex_str1, 16) ^ int(hex_str2, 16)
    return bytes.fromhex(hex(xor_result)[2:]).decode('utf-8')


hex_str1 = "7378ab6d23940bb2dfb7f631150bc5bd"
hex_str2 = "1514ca0a58b53e81bcc5c5454a62b3c0"
result = hex_xor(hex_str1, hex_str2)
print("Risultato XOR:", result)

#https://bernardoamc.com/ecb-iv-as-key/
#flag{!53cr3t_iv}