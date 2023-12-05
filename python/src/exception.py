'''
module to practice exceptions in python
'''
def ask_for_int():
    '''
    ask for int input and validate same
    '''
    while True:
        try:
            result = int(input("Provide an integer"))
        except TypeError as error:
            print(f"this is not an integer... try again... exception {error}")
            continue
        else:
            print(f"Thank you... int entered is {result}")
            break
        finally:
            print("we are in finally")

def check_exception():
    '''
    check exceptions and how to handle it
    '''
    try:
        # a = 0
        var_a = 3
        var_b = 5
        result = var_b / var_a
    except ZeroDivisionError as error:
        print(f"exception received {error}")
    else:
        print(f"we are in else block - runs only in success case... {result}")
    finally:
        print("this is finally block. runs always with or without an exception")

    print("we are at the end")

def input_and_square():
    '''
    get integer and square it
    '''
    while True:
        try:
            val = -1
            val = int(input("enter number"))
        except TypeError as error:
            print(f"enter correct input.. exception {error}")
            continue
        else:
            print(f"Square of {val} is {val*val}")
            break
        finally:
            if val != -1:
                print(f"we are done----{val}")

if __name__ == "__main__":
    ask_for_int()
    check_exception()
    input_and_square()
