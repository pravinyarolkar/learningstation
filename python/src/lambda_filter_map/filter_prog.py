nums = [1,2,3,4,5,6,7,8,9,10]

data = list(map(print, filter(lambda x:x%2==0, nums)))
print(f"data -- > {data}")

data = list(map(lambda x:x**2, filter(lambda x:x%2==0, nums)))
print(f"data ---- > {data}")