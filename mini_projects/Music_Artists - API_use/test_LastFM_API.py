import unittest
import requests_cache
import LastFM_API
import requests
import json
import time


#activating the cache so that we don't call the API too often 
requests_cache.install_cache()

class MusicAPITest(unittest.TestCase):

    
    def test_top_artists(self):
        #result = 
        self.assertEqual(LastFM_API.top_artists(1)[0], 'The Weeknd' )

    def test_top_tags(self):
        #result =
        self.assertEqual(LastFM_API.top_tags(1, 'The Weeknd')[0][1]
        , 'rnb' )

        #result = 
        self.assertEqual(LastFM_API.top_tags(1, 'Lady Gaga')[0][1], 'pop' )

if __name__ == '__main__':
    unittest.main()
    
