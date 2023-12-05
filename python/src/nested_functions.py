def outer_function():
    print("this is outer function")

    def inner_function():
        print("from inner function")

    inner_function()

# to store address dont use paranthesis so that it will not execute
desc = outer_function

print(desc)
desc()

print("---------|---------|---------|---------")

def outer_function_1():
    print("from outer function")

    def inner_function():
        print("from inner function called with func address")

    return inner_function

func = outer_function

outer_function()
