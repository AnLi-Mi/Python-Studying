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
        result = LastFM_API.top_artists(1)[0]
        self.assertEqual(result, 'The Weeknd' )

    def test_top_tags(self):
        result = LastFM_API.top_tags(1, 'The Weeknd')[0][1]
        self.assertEqual(result, 'rnb' )

        result = LastFM_API.top_tags(1, 'Lady Gaga')[0][1]
        self.assertEqual(result, 'pop' )

    def test_rate_limit_calling(self):
        result =LastFM_API.rate_limit_calls()[0]["artists"]["artist"][0]["name"]
        self.assertEqual(result, 'The Weeknd')

if __name__ == '__main__':
    unittest.main()
    
