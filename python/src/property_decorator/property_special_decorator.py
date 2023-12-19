class Item:
    def __init__(self):
        self.price 
        # = price
        # self.__cost = price

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, price):
        self.price = price
    
    @price.deleter
    def price(self):
        del self.price

    def get_price(self):
        return self.price
    

obj = Item(5000)
print(obj.price)

obj.price = 5500
print(obj.price)

obj.__cost = 2000
print(obj.__cost)