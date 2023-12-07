# yield is the keyworkused in generator
# generators are the lazy iterator

def get_val():
    result = 1
    while True:
        yield result # execution halts here till we have next call to read data
        result *= 3

values = get_val()

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))