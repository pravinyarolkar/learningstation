def utils():
    print("Hello World Utils Function")

if __name__ == "__main__":
    utils()
    print(f"file is directly running - {__name__}")
else:
    print(f"module {__name__} is getting imported")