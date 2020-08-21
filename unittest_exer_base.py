class Circle:
    
    import math
    
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        import math
        area = (math.pi)*(self.radius**2)
        print ("The area of this circele is {} square units".format(round(area,2)))
        return area
    
    def perimeter(self):
        import math
        perimeter = 2*(math.pi)*self.radius
        print ("The perimeter of this circele is {} units".format(round(perimeter,2)))
        return perimeter
    
    def area_ins_reg_hex(self):
        import math
        area_ins_hex =(3*(self.radius**2)*(math.sqrt(3)))/2
        print ("The area of a regular hexagon inscribed in this circele is {} square units".format(round(area_ins_hex,2)))
        return area_ins_hex
    
    def area_des_reg_hex(self):
        import math
        area_des_hex =2*(self.radius**2)*(math.sqrt(3))
        print ("The area of a regular hexagon desscribed on this circele is {} square units".format(round(area_des_hex,2)))    
        return area_des_hex
