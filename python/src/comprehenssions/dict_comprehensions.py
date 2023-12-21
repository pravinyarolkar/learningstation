d = {i : i+10 for i in range(10)}
print(d)

d = {x:y for x in range(10) for y in range(10) if x!=y and x<y}
print(d)

'''
Dictionary comprehensions
In Python, dictionary comprehensions are very similar to list comprehensions – only for dictionaries. They provide an elegant method of creating a dictionary from an iterable or transforming one dictionary into another.

The syntax is similar to that used for list comprehension, namely {key: item-expression for item in iterator}, but note the inclusion of the expression pair (key:value).

Let’s look at a simple example to make a dictionary. The code can be written as

dict([(i, i+10) for i in range(4)])
which is equivalent to:

{i : i+10 for i in range(4)}
In both cases, the return value is:

{0: 10, 1: 11, 2: 12, 3: 13}
This basic syntax can also be followed by additional for or if clauses: {key: item-expression for item in iterator if conditional}.

Using an if statement allows you to filter out values to create your new dictionary.

For example:

{i : i+10 for i in range(10) if i > 5}
Returns:

{6: 16, 7: 17, 8: 18, 9: 19}
Similar to list comprehensions, dictionary comprehensions are also a powerful alternative to for-loops and lambda functions. For-loops, and nested for-loops in particular, can become complicated and confusing. Dictionary comprehensions offer a more compact way of writing the same code, making it easier to read and understand.

Nested dictionary comprehension
In Python, dictionary comprehensions can also be nested to create one dictionary comprehension inside another.

For example:

{(k, v): k+v for k in range(2) for v in range(2)}
Returns:

{(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 2}
Take care when using nested dictionary comprehensions with complicated dictionary structures. In such cases, dictionary comprehensions also become more complicated and can negate the benefit of trying to produce concise, understandable code.
'''