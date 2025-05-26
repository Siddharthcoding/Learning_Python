import random

def game():
    print("You are palying the game...")
    score = random.randint(1, 62)  # Simulating a game that returns a random number between 1 and 62
    print(f"Your score: {score}")

    with open("highscore.txt") as f:
        highScore = f.read().strip()  
        if(highScore != ""):
            highScore = int(highScore)
        else:
            highScore = 0

    if(score  > highScore):
        with open("highscore.txt", "w") as f:
            f.write(str(score))
        print("Congratulations! You have set a new high score!")
    
    return score

game()