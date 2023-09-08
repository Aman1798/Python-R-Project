# Project1 = Snake-Water-Gun or Rock-Paper-Scissor
import random


def gameWin(Computer, you):
    # If two value are equal, it is a tie!
    if Computer == you:
        return None
    # Check for all possibilities, when Computer chooses s
    elif Computer == "s":
        if you == "w":
            return True
        elif you == "g":
            return False
    # Check for all possibilities, when Computer chooses w
    elif Computer == "w":
        if you == "s":
            return False
        elif you == "g":
            return True
    # Check for all possibilities, when Computer chooses g
    elif Computer == "g":
        if you == "s":
            return True
        elif you == "w":
            return False


print("Computer Turn: Snake(s), Water(w) or Gun(g)?")
randNO = random.randint(1, 3)
if randNO == 1:
    Computer = "s"
elif randNO == 2:
    Computer = "w"
elif randNO == 3:
    Computer = "g"

you = input("Your Turn: Snake(s), Water(w) or Gun(g)? \n")

a = gameWin(Computer, you)

print(f"Computer chose {Computer}")
print(f"You chose {you}")

if a == None:
    print("Draw, Play Again")
elif a:
    print("You Win")
else:
    print("You Lose")
