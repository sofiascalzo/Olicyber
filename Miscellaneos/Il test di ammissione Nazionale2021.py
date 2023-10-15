#!/bin/env python3

# pip3 install pwntools
from pwn import remote, context


def solve(mosse, stato):
    res = []

    for riga in range(len(mosse)):               # Itera lungo le righe di mossa
        #while colonna in range(len(mosse[riga])):  # Itera lungo le colonne di mossa
        indexLettera=mosse[riga][0]          #prendo in considerazione solo la prima lettera di ogni riga perchè il resto viene di conseguenza
        if stato[indexLettera] < 5:
            res.extend([riga+1] * (5 - stato[indexLettera]))

    res_string = " ".join(map(str, res))  # Trasforma la lista in una stringa separata da spazi
    return res_string
    

r = remote("test.challs.olicyber.it", 15004)
context.log_level = 'debug'
r.recvlines(20)

livello = r.recvline()
while livello.startswith(b"Livello"):
    stato = [int(_) for _ in r.recvline(False).decode().split()]
    mosse = []
    while True:
        s = r.recvline(False).decode()
        if s == "":
            break
        mosse.append(["ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(_) for _ in s.split()])
        print("mosse:  ", mosse)  # mosse matrice (lista di liste)

    res = solve(mosse, stato)
    r.sendline(res)
    r.recvlines(2)
    livello = r.recvline()

#si poteva fare sicuramente meglio ma mi sono comlicata la vita
#flag{questo_era_facile}