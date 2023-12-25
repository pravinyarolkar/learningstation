data = [x*x for x in range(10,50,2)]
print(data)

data = [f"one:{x}" for x in range(1,10,3)]
print(data)

def func(x):
    return x-2

data = [func(x) for x in range(1,30,3)]
print(data)

import math

# nested
d = [x for x in range(1,5,1) if x % 2 != 1]
print(d)

d = [(x,y) for x in range(1,10,1) for y in range(1,10,1) if x!=y and x>y]
print(d)
'''
for x in range(1,10,1):
    for y in range(1,10,1):
        if x != y and x > y:
            print((x,y))
'''


