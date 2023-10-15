from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
import mpmath
mpmath.mp.dps=60

n = 24115724050507199493712762654520929936774925131059332140712511092518570415243144493303620895076999217579151352098005641220254789662082249122039429593281075763473867243116281108360849599370337166659005719677959315594442881058620733458846158693288519442417046197499609227262971291046951868872967724331630614810942937943136630611188831606642913190132779641441613453701616908620598504762030351385284494949746449796839814492726493862301122366764136396286534656293577211209070238444918749907377203907983536318913476902109610454777572292382794615391425461099601480360030664640184539023460489362835787186494390857887931724561
ct = 3339891666664090373900104605188092714288004578913068591061618601501728384543458885590673450917778514384162355873893

#e = phi+3
#d = (phi+3, -1, phi) -->phi%phi=0
#d = (3, -1, phi) 3 molto piccolo, m< n^1/e --> modulo trascurabile
#mpmath per svolgere potenze modulari con numeri decimali
#flag = pow(ct, 1/3, n)

e=3
flag=mpmath.power(ct, mpmath.mpf(1)/mpmath.mpf(e))%n
ptm = long_to_bytes(int(flag))
print (ptm)

link per farlo funzionare senza librerie strane        
https://github.com/d4rkvaibhav/picoCTF-2018-Writeups/blob/master/Cryptography/SAFERSA/rsa.py
https://www.dcode.fr/rsa-cipher