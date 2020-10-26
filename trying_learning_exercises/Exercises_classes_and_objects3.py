class Store:

    def __init__(self, name):
        self.name= name
        self.itmes=[]


    def add_item(self, name, price):
        item = {"name": name, "price": price} 
        self.itmes.append(item)

    def stock_price(self):
        total = sum([item["price"] for item in self.itmes])
        return total


store1=Store("Store's Name")

print(store1.name)
store1.add_item("Apple", 3.5)
print(store1.stock_price())

#-------------------------------------------------------------------

class ClassTest:
    def instance_method(self): #it has self as a first parameter so it's na 'instance method'  
        print (f'This in an instance method of {self}')

    @classmethod
    def class_method(cls): #it has cls as a first parameter so it's a 'class' method
        print (f'This in an class method of {cls}')


test1 = ClassTest() #the object is created even without __init__ method

ClassTest.instance_method(test1) #calling the instance method option1
test1.instance_method() #calling the instance method option2

ClassTest.class_method() # calling the class method - only option


        

         
