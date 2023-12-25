x = [1,2,3,1,2,3]

print(x)

x.append(4)
print(x)

x.append([11,22])
print(x) # [1, 2, 3, 4, [11, 22]]

x.remove([11,22]) # removing sub list

x.extend([11,22])
print(x) # [1, 2, 3, 4, 11, 22]

print(x.index(11)) # 4

print(x.insert(2, 'inserted'))
print(x)

ss = set(x)
print(f"set - {ss}") # duplicate items will be removed and unique items will be kept while converting to set

tt = tuple(x)
print(f"tuple - {tt}")

print(f"before pop - {x}")
x.pop(1)
print(f"after pop - {x}")

x.remove('inserted')
print(x)

x.reverse()
print(x)

x.sort()
print(x)