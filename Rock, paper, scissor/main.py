'''
-1 for rock
1 for paper
0 for scissor
'''
import random

# Randomly choose a number for the computer
computer = random.choice([-1, 1, 0])
you = input("Enter your choice: ")
youDict = {"r": -1, "p": 1, "s": 0}
reverseDict = {-1: "Rock", 1: "Paper", 0: "Scissor"}
youNum = youDict[you]

print(f"Computer chose: {reverseDict[computer]}")
print(f"You chose: {reverseDict[youNum]}")

if(computer == youNum):
    print("It's a tie!")
else:
    if(computer == -1 and youNum == 1):
        print("You win!")
    elif(computer == -1 and youNum == 0):
        print("You lose!")
    elif(computer == 1 and youNum == -1):
        print("You lose!")
    elif(computer == 1 and youNum == 0):
        print("You win!")
    elif(computer == 0 and youNum == 1):
        print("You lose!")
    elif(computer == 0 and youNum == -1):
        print("You win!")
    else:
        print("Something went wrong!")
