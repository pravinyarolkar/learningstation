# set
# is unordered 
# is mutable
# is unique elements - don't add duplicate elements

s = set()

print(type(s))

s.add(10)
s.add('1')
s.add(112)
s.add('A')
s.add(123)
s.add(1.1)

print(s)

s.add(123)
s.add(123)

s1 = set()

s1.add(190)
s1.add('A')
s1.add(112)
s1.add('1')
s1.add(132)
s1.add(12.32)

print(s1)

res = s.intersection(s1)
print(type(res), res)
print(type(res), s.symmetric_difference(s1))
print("Union -", s.union(s1))
s2 = {'A', 1.1}
print(s2.issubset(s))
sc = s.copy()
print(sc) # {112, '1', 1.1, 'A', 10, 123}

sc.discard(112)
print(sc)

print(s.issuperset(s2))

