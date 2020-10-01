import requests
import json

API_KEY = '59df0d91a02d6acff62b031edede3254'
USER_AGENT = 'TestujeAPI-Anna'

def jsonprint(response):
    response = json.dumps(response, sort_keys=True, indent=4)
    print(response)



def lastfm_get(payload):
    headers = {'user-agent': USER_AGENT}
    url = 'http://ws.audioscrobbler.com/2.0/'

    
    payload['api_key'] = API_KEY
    payload['format'] = 'json'
    

    response = requests.get(url, headers=headers, params=payload)
    return response

jsonprint(lastfm_get({'method':'chart.gettopartists'}).json())

