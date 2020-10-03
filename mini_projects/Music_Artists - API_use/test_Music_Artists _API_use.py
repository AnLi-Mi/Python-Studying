import unittest
import Music_Artists_API_use.py as MAA

class MusicAPITest(unittestTestCase):

    
    def test_top_artists(self):
        result = MAA.top_artists(1)
        self.assertEqual(result, "Postion 1 - Lady Gaga" )
        
        

    
