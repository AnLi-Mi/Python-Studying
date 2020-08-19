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
            



