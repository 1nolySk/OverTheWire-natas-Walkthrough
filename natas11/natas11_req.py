#!/usr/bin/python3

import requests
import binascii
from requests.auth import HTTPBasicAuth

Auth = HTTPBasicAuth('natas11', 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK')
headers = {'content-type': 'application/x-www-form-urlencoded'}
url = 'http://natas11.natas.labs.overthewire.org/'

r = requests.get(url, auth = Auth, headers = headers)

if r.status_code != requests.codes.ok:
	raise ValueError("Coudn't connect")
else:
	print('Connected')


print("Enter new cookie : ", end='')
c = input().strip()

cookies = dict(data=c)

r = requests.post(url, auth = Auth, headers = headers, cookies = cookies)
	
print(r.content)
