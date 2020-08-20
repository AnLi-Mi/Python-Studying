import unittest
import Exercises_classes_and_objects.py as e

class TestBase(unittest.TestCase):

    def test_area(self):
        result = e.area(5)
        self.assertEqual(result, 78.54 )

    def test_perimeter(self):
        result = e.perimeter(5)
        self.assertEqual(result, 31.42 )
        
    def test_area_ins_reg_hex(self):
        result = e.area_ins_reg_hex(5)
        self.assertEqual(result, 64.95)

    def test_area_des_reg_hex(self):
        result = e.area_des_reg_hex(5)
        self.assertEqual(result, 86.6 )
