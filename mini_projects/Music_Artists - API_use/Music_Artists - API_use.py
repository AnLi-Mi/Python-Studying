import requests
import json
import time
import requests_cache

#activating the cache so that we don't call the API too often 
requests_cache.install_cache()


# setting up a variables with the api key and requested user agent
API_KEY = '59df0d91a02d6acff62b031edede3254'
USER_AGENT = 'TestujeAPI-Anna'

# function displaying the json response in a more readable way
def jsonprint(response):
    response = json.dumps(response, sort_keys=True, indent=4)
    print(response)


# making the API call from lastfm, payload is a dictionary type variable (it will usually contain the method key with its value)
def lastfm_get(payload):

    headers = {'user-agent': USER_AGENT}
    url = 'http://ws.audioscrobbler.com/2.0/'

    # adding necessary keys to the payload dictionary
    payload['api_key'] = API_KEY
    payload['format'] = 'json'
    

    response = requests.get(url, headers=headers, params=payload)
    return response.json()


# function dispalying given number of top artist's names 
def top_artists(number_of_first_top):
    print (f'TOP {number_of_first_top} artists are:')
    #calling api
    r=lastfm_get({'method':'chart.gettopartists'})
    #seting varioables for looping through result pages and arists positions to fetch name key
    page = 1
    # 'total' is a number of all pages
    last_page= int(r['artists']['@attr']['total'])
    position = 1
    # there is 50 results per page
    last_position = 50
    
    
    # looping through the pages
    while page < last_page +1:
        # adding page attribute to the api call
        result = lastfm_get({'method':'chart.gettopartists', 'page':page})
        # looping through artists positions on the given page
        while position < last_position:
            # on each page the index of position starts from 1 so I need to amend it adding indexes from previous pages
            print(f"Postion {position+49*(page-1)} - {result['artists']['artist'][position]['name']}")
            position+=1
            # stop looping through positions when we reach given number of artists
            if (position+49*(page-1))==number_of_first_top+1:
                break 
        # stop looping through pages when we reach given number of artists
        if (position+49*(page-1))==number_of_first_top+1:
                break    
        position=1     
        page+=1
        
        
def rate_limit_calls():

    responses = []

    page = 1
    total_pages = 1

    while page <= total_pages:
        payload = {
            'method': 'chart.gettopartists',
            'limit': 50,
            'page': page
        }

        # print some output so we can see the status
        #print(f"Requesting page {page}/{total_pages}")

        response = lastfm_get(payload)

        # extract pagination info
        #page = int(response['artists']['@attr']['page'])
        #total_pages = 2

        # append response
        responses.append(response)

        # if it's not a cached result, sleep
        if not getattr(response, 'from_cache', False):
            time.sleep(0.25)

        # increment the page number
        page += 1


    return responses

# function displaying top tags of given artist
def top_three_tags(number_of_tags, aritsts_name):
    
    print (f'Top {number_of_tags} tags assigned to {aritsts_name} are:')
    
    top_three_tags = []

    
    all_tags = lastfm_get({'method': 'artist.getTopTags','artist':{aritsts_name}})
    i=0
    while i<number_of_tags+1:
        tag=all_tags["toptags"]["tag"][i]["name"]
        top_three_tags.append([i+1, tag])
        i+=1

    for tag in top_three_tags:
        print (f'{tag[0]} - {tag[1]}')

   


top_three_tags(5,'Lana Del Rey')
