import unittest
import unittest_exer_base

class TestBase(unittest.TestCase):

    def test_area(self):
        result = unittest_exer_base.area(5)
        self.assertEqual(result, 78.54 )

    def test_perimeter(self):
        result = unittest_exer_base.perimeter(5)
        self.assertEqual(result, 31.42 )
        
    def test_area_ins_reg_hex(self):
        result = unittest_exer_base.area_ins_reg_hex(5)
        self.assertEqual(result, 64.95)

    def test_area_des_reg_hex(self):
        result = unittest_exer_base.area_des_reg_hex(5)
        self.assertEqual(result, 86.6 )
