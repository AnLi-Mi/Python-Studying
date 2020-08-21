import unittest
import unittest_exer_base as u

class TestBase(unittest.TestCase):

    def test_area(self):
        obj1 = u.Circle(5)
        result = u.Circle.area(obj1)
        self.assertEqual(result, 78.54 )

    def test_perimeter(self):
        obj1 = u.Circle(5)
        result = u.Circle.perimeter(obj1)
        self.assertEqual(result, 31.42 )
        
    def test_area_ins_reg_hex(self):
        obj1 = u.Circle(5)
        result = u.Circle.area_ins_reg_hex(obj1)
        self.assertEqual(result, 64.95)

    def test_area_des_reg_hex(self):
        obj1 = u.Circle(5)
        result = u.Circle.area_des_reg_hex(obj1)
        self.assertEqual(result, 86.6 )


    def test_Years(self):
        obj1 = u.Years('1555')
        result=u.Years.int_rom_conv(obj1)
        self.assertEqual(result, "MDLV" )
        
        
