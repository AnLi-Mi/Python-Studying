class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r}, ({self.connected_by})" #!r is adding the quote signs around the variable


    def disconnect(self):
        self.connected = False
        return f"{self.name} is disconnected."

    def connect(self):
        self.connected = True
        return f"{self.name} is connected."
        


printer = Device("Printer", "USB")
print(printer)

print (Device.disconnect(printer))

class Printer(Device): #creating a child class Printer from parent class Device
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)#we are calling a method from the parent class, no self!
        self.capacity = capacity
        self.remaning_pages = capacity # we will be modifying this paramater later

    def __str__(self):
        return f'{super().__str__()}, {self.remaning_pages} reminig pages'

    def printing(self, pages):
        if not self.connected:
            return f'{self.name} is not connected'
        else:
            return f'Printing {pages} pages. Remining pages : {self.remaning_pages - pages}.'

printer1 = Printer("Xerox", "USB", 1000)
print (printer1)
print (printer1.printing(200))
print (printer1.disconnect())
print (printer1.printing(100))
print (printer1.connect())
print (printer1.printing(100))

printer1.print()

