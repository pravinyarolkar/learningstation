class Book():
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price
    
    def __str__(self):
        return f"This is {self.name} by {self.author} at price {self.price}"
    
    def __len__(self):
        return len(self.name)
    
    def __del__(self):
        return f"Object is deleted with book name {self.name}"    

if __name__ == "__main__":
    obj = Book("Python Rocks", "Auther", "2000")

    print(obj)
    # print(obj.__str__()) # works same way
    print(len(obj))
    
    del obj

    try:
        print(obj)
    except NameError as e:
        print(f"obj is not defined - error - {e}")