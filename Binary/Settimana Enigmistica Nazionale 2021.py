stringa_numeri = "500003080003040000780000090001200000000001960007000032000400500002009000090120006"

# crea la matrice vuota
matrice = [[0 for j in range(9)] for i in range(9)]

# riempi la matrice con i numeri dalla stringa
for i in range(9):
    for j in range(9):
        matrice[i][j] = int(stringa_numeri[i*9+j])

# stampa la matrice
for riga in matrice:
    print(riga)


#flag{497621219865765123463954788243759568411783629468571335784}
