from random import randint

player = input("Hello, what's your name?")
cguess = randint(1,10)

guesses = 4
print("I have guessed a number from 1 to 10.")

while guesses != 0:
    guess = int(input("Guess the number!\n"))
    if guess == cguess:
        print("You made it.. The answer is "+ str(cguess))
        break
    elif guess > cguess:
        print("Your guess is too high...")
        guesses -= 1
    elif guess < cguess:
        print("Your guess is too low...")
        guesses -= 1

if guesses == 0:
    print("You are out of chances! \n The number is " + str(cguess))