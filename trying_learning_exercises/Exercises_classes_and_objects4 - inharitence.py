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

printer1 = Printer("Xerox", "USB", 1000)
print (printer1)
