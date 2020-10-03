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

if __name__ == '__main__':
    unittest.main()
    
