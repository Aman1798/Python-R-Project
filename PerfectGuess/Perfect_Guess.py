# The perfect guess
import random

randNumber = random.randint(1, 100)

userGuess = None
guesses = 0
while userGuess != randNumber:
    userGuess = int(input("Enter your guess:"))
    guesses += 1
    if userGuess == randNumber:
        print(f"Congratulations! The number was indeed {randNumber}.")
    else:
        if userGuess > randNumber:
            print("You guessed it wrong!\n**Try a smaller number**")
        else:
            print("You guessed it wrong!\n**Try a larger number**")

print(f"You guessed the number in {guesses} guesses.")

with open("highScore.txt", "r") as f:
    highScore = int(f.read())

if guesses < highScore:
    print(f"Congratulations! {randNumber} This is the new Highest Score!")
    with open("highScore.txt", "w") as f:
        f.write(str(guesses))
elif guesses > highScore:
    print(f"You missed the highest score by {guesses - highScore} guesses.")

else:
    print("Congratulations! You just equaled the highest score.")
