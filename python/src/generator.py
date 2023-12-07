def get_cube():
    nums = [1,2,3,4,5,6,7,8]
    result = []

    for i in nums:
        # print(i)
        result.append(i**3)
    return result

print(get_cube())

for data in get_cube():
    print(data)

# below is with yield

def get_cube_with_yield(): # this is generator function
    nums = [1,2,3,4,5,6,7,8]
    
    for i in nums:
        # print(i)
        print("before yield - holding execution till next call...")
        yield i**3 # halts execution till next call to get value

print(get_cube_with_yield())

result = []

for i in get_cube_with_yield():
    print(f"after call to get_cube_with_yield() function data is - {i}")
    result.append(i)

print(result)