"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 4 guesses to guess the number correctly.
After each wrong guess, the user will be told whether to
guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
import random


def run_game():
    answer = random.randint(1, 100)
    print(f"I'm thinking of a number between 1 and 100 {answer}")
    MaxTries = 25
    attempts = 0
    oldguess = 50
    newguess = 25
    guess = 50
    while True:
#        guess = int(input("Guess a number: "))
        attempts +=1
        oldguess = newguess
        if newguess == answer:
            print(f"Bingo, {answer} this is correct answer, you took {attempts} attempts to guess it right")
            return
        elif MaxTries == attempts:
            print(f"You failed, number of attempts left {MaxTries - attempts}")
            return
        elif newguess < answer:
            print(f"Guess higher number, number of attempts left {MaxTries - attempts}")
            newguess = int(guess+(100-oldguess)/2)
            print(newguess)
        elif newguess > answer:
            print(f"Guess lower number, number of attempts left {MaxTries - attempts}")
            newguess = int(guess-oldguess/2)
            print(newguess)
        else:     
            print(f"the number is {answer}, number of attempts left {MaxTries - attempts}")
            
run_game()
