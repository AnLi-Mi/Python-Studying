class Store:

    def __init__(self, name):
        self.name= name
        self.itmes=[]


    def add_item(self, name, price):
        dic_of_items = {"name": name, "price": price} 
        self.items.append(dic_of_items)

    def stock_price(self):
        total = sum(item["price"] for item in self.item)
        return total


store1=Store("Store's Name")

print(store1.name)
store1.add_items("Apple", 3.5)
print(store1.stock_price())
