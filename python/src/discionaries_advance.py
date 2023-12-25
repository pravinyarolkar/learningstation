d = dict()

print(type(d))

d.update({"k1":1})
snew  = {'k2':2, 'k3':3, 'k4':4}

d.update(snew)

print(d)

for k, v in d:
    print(f"Key - {k}")
    print(f"Value - {v}")

d1 = {x**2:x for x in range(10)}
print(d1)

d2 = {k:v**2 for k,v in zip(['a','b'],range(2))}
print(d2)

# how to use zip
for x,y,z in zip('abcd', range(1,20,3), range(1,20,2)):
    print(f"x = {x}, y = {y}, z = {z}")

for i in d1.__iter__():
    print(f"........... {i}")
for k in d1.items(): #return sets
    print(k)
