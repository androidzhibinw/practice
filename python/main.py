import json,requests

url='http://localhost:5000/api/register'
payload = {'some': 'data'}

r = requests.post(url, data=json.dumps(payload))
