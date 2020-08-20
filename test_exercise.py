import unittest
import unittest_exer_base

class TestBase(unittest.TestCase):

    def test_area(self):
        result = unittest_exer_base.area(5)
        self.assertEqual(result, 78.54 ) 
