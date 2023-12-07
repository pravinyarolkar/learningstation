logfile_name = "./logger.txt"

def logging(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"result is {result}")
        f = open(logfile_name, '+a')
        f.write(f"{func.__name__} : result is {result}\n")
        f.close()
        return result

    return wrapper

@logging
def getSum(x, y):
    return x+y

print(getSum(10,22))