age = int(input("Enter your age: "))

# If statement no. 1
if(age % 2 == 0):
    print("You are even.")
# End of if statement no. 1

# If statement no. 2
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
# End of if statement no. 2

print("End of program.")
