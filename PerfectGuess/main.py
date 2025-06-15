from random import randint

randomNumber = randint(1, 100)

def guess_number():
    guess = None
    while guess != randomNumber:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        elif guess < randomNumber:
            print("Too low! Try again.")
        elif guess > randomNumber:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")

guess_number()
        
