import helloWorldUtils

print("this is at start and outside function")

def helloWorld():
    str1 = "hello world"
    print("This is Hello World program")
    print(f"This is {str1} program")

if __name__ == "__main__":
    helloWorld()
    print("we are in main function")