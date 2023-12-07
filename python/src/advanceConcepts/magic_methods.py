from typing import Any

class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, obj):
        return Vector(self.x + obj.x, self.y + obj.y)
    
    def __repr__(self) -> str:
        return f"X:{self.x}, Y:{self.y}"
    
    def __len__(self):
        return 10 # hard coding for now
    
v = Vector(10,20)
v2 = Vector(5,15)

v3 = v + v2

print(v3)
print(len(v3))

# __getitem__
# __setitem__
# __init__
# __contains__

class MyArray:
    def __init__(self, item) -> None:
        self.arr = item

    def __getitem__(self, index):
        if len(self.arr) == 0:
            return -1
        else:
            return self.arr[index]

    def __setitem__(self, index, item):
        print(f"length is {len(self.arr)} and index is {index}")
        self.arr[index] = item
        print("Done. Item set.")

    def __contains__(self, item):
        if item in self.arr:
            return True
        else:
            return False

obj = MyArray([1,2,3,4,5])

print(obj[0])
obj[0] = 11
print(obj[0])

print(10 in obj)
print(3 in obj)


# __lt__, __gt__, __le__, __ge__, __eq__, and __ne__ magic methods
# Comparative operators can be used to compare between the object’s attributes. 
# The available methods are __lt__, __gt__, __le__, __ge__, __eq__, and __ne__ that performs less than,
# greater than, less than or equal to, greater than or equal to, equal to, 
# and not equal to operations respectively.


class Data:
    def __init__(self, val) -> None:
        self.val = val

    def __call__(self, num):
        return self.val * num
    
obj = Data(5)

print(obj(10))


# Summary #
# In this post, we have seen how to leverage the use of magic methods in python to provide additional functionalities to the class objects without any overhead.
# The __add__ method is used to add two object’s attributes
# The __getitem__ and __setitem__ methods are used to set and get the items of an object’s container attributes
# The __repr__ method is used to print the object as a string
# The __len__ method is used to find the length of the object’s attributes
# __lt__, __gt__, __le__, __ge__, __eq__, and __ne__ methods are used for comparison of object’s attributes
# __contains__ method is used for membership validation
# __enter__ and __exit__ methods are used with the ‘with’ block in the python
# __call__ method is used to use the object as a method.
# __iter__ method is used to generate generator objects using the object

