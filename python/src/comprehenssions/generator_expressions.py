# generator example

def get_even_nums(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

gen = get_even_nums

# print(get_even_nums(20)) # <generator object get_even_nums at 0x0000021959248040>

data = []
for i in gen(20):
    data.append(i)
print(data)

# as a expressions we can write it as below

gen_func = (x for x in range(20) if x % 2 == 0)
# gen_func() # TypeError: 'generator' object is not callable

for i in gen_func:
    print(i)

print(type(gen), type(get_even_nums))

'''
Generator expressions versus list comprehensions
The syntax of generator expressions is strikingly similar to that of list comprehensions, the only difference is the use of round parentheses as opposed to square brackets.

For example, a generator expression can be written as:

(i ** 2 for i in range(10) if i > 5)
Compare that to a list comprehension, which is written as:

[i ** 2 for i in range(10) if i > 5]
Where they differ, however, is in the type of data returned. While a list comprehension will return the entire list, a generator expression will return a generator object. Although values are the same as those in the list, they are accessed one at a time by using the next() function.
'''