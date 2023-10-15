import pyshark
cap = pyshark.FileCapture('capture.pcapng')
d = {} #dizionario per salvare l'archivio key: index , data in hex
for packet in cap:
    if 'dns' in packet: #filtra per protocollo dns
        try:
            print(packet.dns.qry_name) #print query name
            stringp = packet.dns.qry_name 
            stringp = stringp.split(".") #splitta la stringa per ricavare index-data in hex-attacker.eve
            print(stringp)
            index = stringp[0] #index pacchetto
            datap = stringp[1] #data 
            #print(int(index,16))
            d[int(index,16)] = datap #salvo nel dizionario i dati di un pacchetto e il suo indice (in questo modo sorto i pacchetti e evito che vengano salvate duplicazioni)


        except:
            continue


print(d) #stampa dizionario
f = open('file.txt',"wb") 
for i in range(len(d)):
    f.write(bytes.fromhex(d[i])) #salvo il dizionario sul file e converto i dati in bytes


#successivamente: il file creato in realta' e' uno zip (lo vedo dal comando file su bash)
#estraggo il contenuto dal file (rinomino il file.txt in file.zip o uso un comando per fare unzip)
#flag nel file gatto flag
