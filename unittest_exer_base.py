def area(r):
    import math
    area_c= (math.pi)*(r**2)
    return "The area of this circele is {} square units".format(round(area,2))

def perimeter(r):
    import math
    perimeter_c= 2*(math.pi)*r
    return "The perimeter of this circele is {} units".format(round(perimeter,2))

def area_ins_reg_hex(r):
    import math
    area_ins_hex =(3*(r**2)*(math.sqrt(3)))/2
    return "The area of a regular hexagon inscribed in this circele is {} square units".format(round(area_ins_hex,2))

def area_des_reg_hex(r):
    import math
    area_des_hex =2*(r**2)*(math.sqrt(3))
    return "The area of a regular hexagon desscribed on this circele is {} square units".format(round(area_des_hex,2))
