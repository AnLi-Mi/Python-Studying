import requests

headers = {'user-agent': 'TestujeAPI-Anna'}

r_api = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers)

API_KEY = '59df0d91a02d6acff62b031edede3254'
USER_AGENT = 'TestujeAPI-Anna'

headers = {
    'user-agent': USER_AGENT
}

payload = {
    'api_key': API_KEY,
    'method': 'chart.gettopartists',
    'format': 'json'
}

r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
print(r.status_code)


