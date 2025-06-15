def myFunc():
    print("Hello world")


# This code is in a separate module named 'module.py'


if __name__ == "__main__":
    # If this code is directly executed by running the file it is present in
    print("We are directly running this code")
    myFunc()
    print(__name__)