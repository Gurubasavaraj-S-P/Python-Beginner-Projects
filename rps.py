from random import randint

choices= ["Rock", "Paper", "Scissor"];

comp = choices[randint(0,2)]

player = False

player = input("Choose One, Rock, Paper, Scissor.")

if player not in choices:
    print("Incorrect input!")
    player = input("Choose One, Rock, Paper, Scissor.")
if player == comp:
    print("It's a draw..")
elif player == "Rock":
    if comp == "Paper":
        print("Computer has chosen " + comp)
        print("You Lost...")
    else:
        print("Computer has chosen " + comp)
        print("You Won...")
elif player == "Paper":
    if comp == "Scissor":
        print("Computer has chosen " + comp)
        print("You Lost...")
    else:
        print("Computer has chosen " + comp)
        print("You Won...")
elif player == "Scissor":
    if comp == "Rock":
        print("Computer has chosen " + comp)
        print("You Lost...")
    else:
        print("Computer has chosen " + comp)
        print("You Won...")    