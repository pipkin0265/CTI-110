#Guessing number game with a menu
#10/27/2020
#CTI-100 P5HW1 - Random Number
#Michael Pipkin II

'''
Pseudocode:

1. Input 1 or 2 to play game or exit.
2. If input is 1, you have 5 attempts to
input number that you think is the guessed number.
3. If guessed wrong then input another number
until you run out of guesses.
4. If win, dispaly Congrats and how many times it too for you to guess.
5. If lose, display You ran out of guesses and what the guessed number was.
'''

import random

def guessTheNumber():
    print("\nLet us play Guess the Number!")
    print("I am thinking of a number between 1 and 100")
    print("Try to guess the number and I will give you hints along the way")
    print("You have at max 5 tries to guess the number")

    secretNumber=random.randint(1,100)   #random number being created

    numTires=0

    while numTires!=5:        #how many attempts you have
        numTires+1
        win=False

        guess=int(input("\nEnter a number between 1 and 100: "))  #input your number you think is the number

        if(guess==secretNumber):
            print("\nCongratulations!!! You win in {} tries.".format(numTires))
            numTires+=1
            win=True
            break

        elif(guess<secretNumber):
            print("Too low! Guess a number higher than {}".format(guess))
            numTires+=1

        else:
            print("Too high! Guess a number lower than {}".format(guess))
            numTires+=1

    if(numTires==5 and win==False):
        print("\nGame Over. You used up all 5 tires!")
        print("The number was {} - better luck next time!".format(secretNumber))

def displayMenu():
    print("1. Play Game")
    print("2. Exit")

    choice=int(input("Enter your choice 1 or 2: "))
    return choice

def main():
    while True:
        userChoice=displayMenu()
        if(userChoice==1):
            while True:
                guessTheNumber()
                again=input("\nDo you wish to play agian? Enter y or n: ")
                if(again=='n'):
                    print()
                    break
        if(again=='n' and userChoice==2):
            break
    print("Goodbye. Hope you enjoyed playing!!")

if __name__ == '__main__':
    main()

        
