age = int(input("Enter your age: "))

# If elif else ladder

if(age >= 18):
    print("You are an adult.")
    print("Good for you!")
elif(age < 0):
    print("Invalid negative age.")
elif(age == 0):
    print("You are a newborn.")
else:
    print("You are a minor.")
    print("Enjoy your childhood!")

print("End of program.")
