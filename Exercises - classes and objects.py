# Exercise 1 - Check if it's triangle:

class Triangle():
    def __init__ (self, angle1, angle2, angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3

    number_of_sides = 3

    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            print ("It's a triangle")
        else:
            print ("It's not a triangle")

my_triangle=Triangle(30,60,90)

my_triangle.check_angles()

print (my_triangle.number_of_sides)

print ('--------------------------------------------------------------')

# Exercise 2 Printing lines of song - like karaooke


class Songs():
    def __init__(self, lyrics):
        self.lyrics= lyrics


    def sing_me_a_song(self):
        for l in self.lyrics:
            print (f'{l} ! ') 


happy_birthday=Songs(["May god bless you, ","Have a sunshine on you,","Happy Birthday to you !"])

happy_birthday.sing_me_a_song()


print ('--------------------------------------------------------------')

# Exercise 3 Printing out the price of chosen menu


class Lunch():
    def __init__(self, menu):
        self.menu=menu

    def menu_price(self):
        if self.menu=="menu1":
            print (f'Your choice: {self.menu} price 12.00')
        elif self.menu=="menu2":
            print (f'Your choice: {self.menu} price 13.00')
        else:
             print (f'Error in menu')



Paul = Lunch("menu1")

Paul.menu_price()

print ('--------------------------------------------------------------')

# Exercise 4 Printing variables of a point in space

class Point3D():
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point=Point3D(1,2,3)

print(my_point)

print ('--------------------------------------------------------------')

# Exercise 5 Turning intiger in to roman number

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
                   1000:'M'}

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
        print(elements)   

        for n in elements: # converting all ememnts to roman numbers
            #n=int(n)
            rom.append(self.int_to_rom_dic[n])
            

        
        print(''.join(rom))

year1=Years('1555')
year1.int_rom_conv()

year2=Years('1919')
Years.int_rom_conv(year2)

    
             



            








    

