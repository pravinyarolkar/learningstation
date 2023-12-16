def print_args(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['keyone'])
    print(kwargs['keytwo'])

    print(f"Number of args - {len(args)}")

print_args(1,"two",1.3,True,keyone="ONE",keytwo="TWO")

import sys

# command line arguments are used as below

# main

print(sys.argv[0]) # here we get file name

# cmd args start from argv[1] and so on

filename = sys.argv[1]

with open(filename, '+a') as f:
    f.write(sys.argv[2])

print(sys.argv) 
print(sys.argv[0])

print(f"length - {len(sys.argv)}")


