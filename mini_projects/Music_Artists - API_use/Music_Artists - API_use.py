import requests
import json
import time
import requests_cache
#from IPython.core.display import clear_output

requests_cache.install_cache()

API_KEY = '59df0d91a02d6acff62b031edede3254'
USER_AGENT = 'TestujeAPI-Anna'





def jsonprint(response):
    response = json.dumps(response, sort_keys=True, indent=4)
    print(response)


# making the API call
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
            position+=1
            if (position+49*(page-1))==number_of_first_top+1:
                break 
        if (position+49*(page-1))==number_of_first_top+1:
                break    
        position=1     
        page+=1
        
        
print ('TOP 100 artists are:')
top_artists(100)

def rate_limit_calls():

    responses = []

    page = 1
    total_pages = 99999 

    while page <= total_pages:
        payload = {
            'method': 'chart.gettopartists',
            'limit': 5,
            'page': page
        }

        # print some output so we can see the status
        print(f"Requesting page {page}/{total_pages}")

        # clear the output to make things neater
        #clear_output(wait = True)

        response = lastfm_get(payload)

        # extract pagination info
        page = int(response['artists']['@attr']['page'])
        total_pages = int(response['artists']['@attr']['totalPages'])

        # append response
        responses.append(response)

        # if it's not a cached result, sleep
        if not getattr(response, 'from_cache', False):
            time.sleep(0.25)

        # increment the page number
        page += 1

        return responses

rate_limit_calls()


import pandas as pd

r0 = responses[0]
r0_json = r0
r0_artists = r0_json['artists']['artist']
r0_df = pd.DataFrame(r0_artists)
r0_df.head()
