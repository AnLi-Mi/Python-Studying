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

#jsonprint(lastfm_get({'method':'chart.gettopartists'}).json())

def loop_through_pages(num_of_pages):
    page = 1
    #position =1
    last_page= num_of_pages
    #artist_name = []

    while page < last_page +1:
        result = lastfm_get({'method':'chart.gettopartists', 'page':page})
        #while position < 51:
         #   artist = result.json()['artists']['artist'][position]['name']
         #   artist_name.append(artist)
       # 
        jsonprint(result)
        page+=1

#print (len(artist_name))
#print('TOP 100 artists:')
#i=1
#for artist in artist_name:
 #   print (f' No {i} - {artist}')
  #  i+=1

#r=lastfm_get({'method':'chart.gettopartists'})
#jsonprint(r.json()['artists']['artist'][2]['name'])

loop_through_pages(3)
