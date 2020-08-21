class Circle:
    
    import math
    
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        import math
        area = (math.pi)*(self.radius**2)
        area = round(area,2)
        print ("The area of this circele is {} square units".format(round(area,2)))
        return area
    
    def perimeter(self):
        import math
        perimeter = 2*(math.pi)*self.radius
        print ("The perimeter of this circele is {} units".format(round(perimeter,2)))
        perimeter = round(perimeter,2)
        return perimeter
    
    def area_ins_reg_hex(self):
        import math
        area_ins_hex =(3*(self.radius**2)*(math.sqrt(3)))/2
        print ("The area of a regular hexagon inscribed in this circele is {} square units".format(round(area_ins_hex,2)))
        area_ins_hex = round(area_ins_hex,2)
        return area_ins_hex
    
    def area_des_reg_hex(self):
        import math
        area_des_hex =2*(self.radius**2)*(math.sqrt(3))
        print ("The area of a regular hexagon desscribed on this circele is {} square units".format(round(area_des_hex,2)))    
        area_des_hex = round(area_des_hex,2)
        return area_des_hex


class Years:

    int_to_rom_dic = {1:'I',
                      2: 'II',
                      3: 'III',
                       4:'IV',
                      5: 'V',
                      6: 'VI',
                      7: 'VII',
                      8: 'VIII',
                      9:'IX',
                       10:'X',
                      20:'XX',
                      30:'XXX',
                    40:'XL',
                    50:'L',
                      60:'LX',
                      70:'LXX',
                      80:'LXXX',
                    90:'XC',
                    100:'C',
                      200:'CC',
                      300:'CCC',
                      400:'CD',
                    500:'D',
                      600:'DC',
                      700:'DCC',
                      800:'DCCC',
                    900:'CM',
                   1000:'M',
                      2000:'MM'}

    def __init__(self, number):
        self.number = number
    

    def int_rom_conv(self):
              
        rom=[] # empty list to populate it with with roman numbers
        elements=[] # empty list to populate with the elements of the sting to turn them to roman numbers
        a=1000 # used to indicate decimal level of a given element 
        i=0 #used to point an index of of a given sting
        while i<len(self.number): # looping through all elements of the string to convert them into decimel format
             y = self.number[i]
             y =int(y)
             x = y*a
             elements.append(int(x))
             a=a/10
             i+=1
        #print(elements)   

        for n in elements: # converting all ememnts to roman numbers
            n=int(n)
            rom.append(self.int_to_rom_dic[n])

        result=(''.join(rom))

        return result






