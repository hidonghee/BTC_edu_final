import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote


os.environ['UPBIT_OPEN_API_ACCESS_KEY'] = 'zNoKwaKvzaxoQl9c8AuVSOoKAXPAK4dG3LdCvPvP'
os.environ['UPBIT_OPEN_API_SECRET_KEY'] = 'Ew8TtCScDYGV5QTOexlhTeoptob0RSCixm32iTr9'

access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
server_url = 'https://api.upbit.com'

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorization = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization,
}

res = requests.get(server_url + '/v1/accounts', headers=headers)
print(res.json())