def my_decorator_func(func):
    def wrapper_func():
        # do something before function call
        print("we are before function call")
        func()
        # do after function call
        print("we are after function call")

    return wrapper_func

@my_decorator_func
def my_func():
    print("we are in my_func")

my_func()