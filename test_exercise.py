import unittest
import unittest_exer_base as u

class TestBase(unittest.TestCase):

    def test_area(self, Circle.radius):
        result = u.Circle.area(5)
        self.assertEqual(result, 78.54 )

    def test_perimeter(self):
        result = u.Circle.perimeter(5)
        self.assertEqual(result, 31.42 )
        
    def test_area_ins_reg_hex(self):
        result = u.Circle.area_ins_reg_hex(5)
        self.assertEqual(result, 64.95)

    def test_area_des_reg_hex(self):
        result = u.Circle.area_des_reg_hex(5)
        self.assertEqual(result, 86.6 )
