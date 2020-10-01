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
    return response.json()



def top_artists(number_of_first_top):
    r=lastfm_get({'method':'chart.gettopartists'})
    page = 1
    last_page= int(r['artists']['@attr']['total'])
    position = 1
    last_position = 50
    
    

    while page < last_page +1:
        result = lastfm_get({'method':'chart.gettopartists', 'page':page})             
        while position < last_position:
            print(f"Postion {position+49*(page-1)} - {result['artists']['artist'][position]['name']}")
           # artist_name.append(artist)
            position+=1
            if (position+49*(page-1))==number_of_first_top+1:
                break 
        if (position+49*(page-1))==number_of_first_top+1:
                break    
        position=1     
        page+=1
        
        
print ('TOP 100 artists are:')
top_artists(100)

