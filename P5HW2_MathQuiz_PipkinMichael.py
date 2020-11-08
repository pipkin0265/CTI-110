#A program that add random numbers or subtracts numbers
#10/28/2020
#CTI-110 P5HW2 - Math Quiz
#Michael Pipkin II

import random

# a funtion to get a random number in a range
def random_generator(low,high):
    r = random.randint(low,high)
    return r
  
# this funtion checks the answers with expected results and return score of a user
def score(expected, answered):
    count=0
    for i in range(0,len(answered)):
        if expected[i]==answered[i]:
            count += 1
    return count

def main():
    print("Welcome to math quiz");
    quiz_type = ['Subtraction', 'Addition']
    quiz_level = ['Easy', 'Intermediate', 'Hard']
    while(True):
        type = int(input("Select quiz type\n1.Subtraction\n2.Addition\n"))
        level = int(input("Select difficulty level\n1.Easy\n2.Intermediate\n3.Hard\n"))
        # based on difficulty level set the range of numbers
        high = 10**level-1
        low = 10**(level-1)-1
        expected = []
        answered = []
        if type == 1:
        # provide ten subtraction questions
            for i in range(0,10):
                # get random numbers
                x = random_generator(low,high)
                y = random_generator(low,high)
                # get the user answer.
                ans = int(input(str(x)+ " - " + str(y)+" = "))
                answered.append(ans)
                expected.append(x-y)
        else:
            # provide ten addition questions
            for i in range(0,10):
                # get random numbers
                x = random_generator(low,high)
                y = random_generator(low,high)
                # get the user answer.
                ans = int(input(str(x)+ " + " + str(y)+" = "))
                answered.append(ans)
                expected.append(x+y)

        # display the details
        print("quiz type: ",quiz_type[type-1])
        print("quiz level: ",quiz_level[level-1])
        total_score = score(expected, answered)
        print("You score:",total_score)
        choice = int(input("Enter 1 to play again: "))
        if(choice!=1):
            break
main()
