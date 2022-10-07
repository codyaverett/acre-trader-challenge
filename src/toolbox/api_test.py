#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth

basic = HTTPBasicAuth('testuser', 'commonpassword')

endpoint = 'http://127.0.0.1:9001/api/v1/'
resource = ['todos', 'todolists']
methods = ['get', 'post', 'put', 'patch', 'delete']

r = requests.get(f'{endpoint}{resource[0]}/', auth=basic)
print(r.content)
print(r.status_code)
