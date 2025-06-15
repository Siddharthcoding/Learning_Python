# The finally block is always executed, regardless of whether an exception occurred or not

def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
    finally:
        print("This block always executes, regardless of whether an exception occurred or not.")

main()