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
    
    if not getattr(response, 'from_cache', False):
            time.sleep(0.25)
            
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
    # there is 50 results per page by default
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

        if not getattr(r, 'from_cache', False):
            time.sleep(0.25)
        
        
def rate_limit_calls():

    responses = []

    page = 1
    # rundom number just to stat the loop
    total_pages = 10 

    while page <= total_pages:
        payload = {
            'method': 'chart.gettopartists',            
            'limit': 50, # as default
            'page': page
        }

        # printing some output so we can see the status
        print(f"Requesting page {page}/{total_pages}")

        response = lastfm_get(payload)

        # extract pagination info for the status display
        page = int(response['artists']['@attr']['page'])
        total_pages = int(response['artists']['@attr']['total'])

        # append response from current page
        responses.append(response)

        # checking if thr result was cached if not - sleep
        if not getattr(response, 'from_cache', False):
            time.sleep(0.25)

        # moving to the next page
        page += 1

    return responses


# function displaying top tags of given artist
def top_tags(number_of_tags, aritsts_name):
    
    print (f'Top {number_of_tags} tags assigned to {aritsts_name} are:')

    #preparing empty list to fill it with tags
    top_three_tags = []

    #calling API with getTopTags method and given artist's name parapeter
    all_tags = lastfm_get({'method': 'artist.getTopTags','artist': aritsts_name})

    #looping through all the tags form the API calling result
    i=0
    while i<number_of_tags:
        #extracting value of each "name" key
        tag=all_tags["toptags"]["tag"][i]["name"]
        #saving the name and the position in results
        top_three_tags.append([i+1, tag])
        i+=1

    for tag in top_three_tags:
        print (f'{tag[0]} - {tag[1]}')

    # checking if thr result was cached if not - sleep
    if not getattr(all_tags, 'from_cache', False):
        time.sleep(0.25)
  


top_tags(5,'Lana Del Rey')

top_tags(3,'The Weekend')
