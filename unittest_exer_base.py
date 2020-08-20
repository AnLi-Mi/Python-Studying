def area(r):
    import math
    area_c= (math.pi)*(r**2)
    x = round(area_c,2)
    return   print(x)

def perimeter(r):
    import math
    perimeter_c= 2*(math.pi)*r
    x = round(perimeter_c,2)
    return print(x)

def area_ins_reg_hex(r):
    import math
    area_ins_hex =(3*(r**2)*(math.sqrt(3)))/2
    x = round(area_ins_hex,2)
    return print(x) 

def area_des_reg_hex(r):
    import math
    area_des_hex =2*(r**2)*(math.sqrt(3))
    x = round(area_des_hex,2)
    return print(x)

area(5)
perimeter(5)
area_ins_reg_hex(5)
area_des_reg_hex(5)
