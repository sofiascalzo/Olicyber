import os
with open('pincodeDEF.txt', 'w') as f:
    pin=''
    for i in range(1000):
        pin += str(i)
        f.writ
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
