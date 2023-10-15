from pwn import *
host = "bowser.cybertrials.it"
port = 30500

while True:
    try:
        r = remote(host, port)
        f = r.recv()
        print(f.decode())
        port+=1
    except:
        print("porta chiusa")
        port+=1
    #r.close()
