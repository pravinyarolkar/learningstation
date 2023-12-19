import random

print(dir(random))
print(type(random.__all__))

for i in range(1,10,2):
    print(random.randint(10,1000))

print(dir(random.Random))
print(random.randrange(2,2000,4))

print(random._inst.randint(22,33))

start = int(input("enter start number - "))
end = int(input("enter end number - "))

if start > end:
    raise ValueError(f"please enter a valid range")

try:
    print(random.randint(start, end))
except Exception as e:
    print("Exception received - {}".format(e))
