# lambda is a anonymous function which will be declared and used inline with fiter and maps

func = lambda x: x**2
print(func(2))

func = lambda x,y: x+y
print(func(10,20))

def func1(x,y):
    return x+y

f = lambda x,y: func1(x,y)
print(f(11,22))

data = []
def func(x,y,z):
    for i in range(x,y,z):
        data.append(i)
    return data
f = lambda x,y,z: func(x,y,z)
print("----->",f(1,10,1))

f = lambda x: list(map(print, func(1,x,1)))
f(5)