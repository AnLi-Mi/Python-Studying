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
