import random

number = random.randint(0, 1000)
chances = 20

while chances > 0:
    guess = int(input("GUESS A NUMBER : "))
    if (guess == number):
        print("YOU WON THE GAME")
        break

    if abs(guess - number) <= 10:
        print("Guess Very Close")
    elif guess > 2*number:
        print("Guess is too large")
    elif guess > number:
        print("Guess is a little large")
    elif guess < number/2:
        print("Guess is too small")
    else :
        print("Guess is a little small")

    chances -= 1

if chances == 0:
    print("YOU LOSE") 