def func(x):
    data = []
    for i in range(x):
        data.append(i)
    print(f"data list is - {data}")
    return data

def func1(data):
    print(f"debug - {data}")
    for i in data:
        data[i] = i**2
        return data
    
data = func(10)

data_list = list(map(print, data))

def func(x):
    return x*x

data = list(map(func, [2,3,4,5]))
print(data)