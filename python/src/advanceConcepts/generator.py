# yield is the keyworkused in generator
# generators are the lazy iterator

def get_val():
    result = 1
    while True:
        yield result
        result *= 3

values = get_val()

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))