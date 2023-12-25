msg = "Hello World"

print(msg.capitalize())
print(msg.count('o'))
print(msg.find('r'))
print(msg.isascii(), msg.isdecimal())
print(msg.lower(), msg.islower())
print(msg.center(20,'-'), "\n", msg.center(20,'A'))
print(msg.endswith('d'), msg.endswith('D'))
print('hello'.islower())
print(msg[-1])
print(msg[1:],"\n",msg[:5], "\n", msg[1:4], "\n", msg[1:8:2], "\n", msg[::-1])
print('hello heritage'.split('e'))