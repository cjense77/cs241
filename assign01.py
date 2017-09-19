# Colin Jensen
# CS 241
# 9/18/17

import random
from random import randint

# Generate a random number and prompt the
# user for guesses until he/she guesses right. 
def playGame():
    num = randint(1,100)
    guesses = 0
    guess = -1
    
    while (guess != num):
        guess = int(input("\nPlease enter a guess: "))

        if (guess < num):
            print("Higher")
        elif (guess > num):
            print("Lower")

        guesses += 1
    
    return guesses

# Initiate game and repeat until user no longer wants to play
def main():
    print("Welcome to the number guessing game!")
    
    seed = input("Enter random seed: ")
    random.seed(seed)
    
    playAgain = True
    while (playAgain):
        guesses = playGame()
        
        print("Congratulations. You guessed it!\n"
              "It took you {0} guesses.".format(guesses))
        
        playAgain = input("\nWould you like to play again (yes/no)? ")
        if (playAgain == "no" or playAgain == "No"):
            playAgain = False
    
    print("Thank you. Goodbye.")
    
if __name__ == "__main__":
    main()