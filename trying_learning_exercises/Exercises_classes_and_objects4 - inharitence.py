class Divice:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r}, ({self.connected_by})" #!r is adding the quote signs around the variable


    def disconnect(self):
        self.connected = False
        return f"{self.name} is disconnected."


printer = Divice("Printer", "USB")
print(printer)

print (Divice.disconnect(printer))
