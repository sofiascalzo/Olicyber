import os
with open('pincode.txt', 'w') as f:
    for i in range(10000):
        pin = str(i).zfill(4)
        f.write(pin + '\n')
print(os.getcwd())

#Da risolvere con Burp:
# intercetto richiesta post
# vado su http history
# tasto destro su send to intruder
# vado sulla bagina di intruder
# opzione simple list
# carico il file di testo generato da questo script
# start attack
# aspetto un messaggio di errore
