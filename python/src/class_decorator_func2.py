from typing import Any


class data:
    def __init__(self, func):
        self.func = func
        self.api = "/api/v1/data/get/resource"

    def __call__(self, *args, **kwargs):
        print("in __call__ function... arg is ",args[0], len(args))

        return self.func(*args, **kwargs)
    
@data
def dummy_func(number):
    print(f"argument is {number}")

if __name__ == "__main__":
    dummy_func(20)