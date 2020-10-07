#Cleaning up the bugs!
#Pipkin II

def main():

    num=int(input(' Please Enter Your Grade: '))      #Asks user to input grade score

    if num <= 100 and num >= 90:                        #If, elif statement that returns letter grade on input
        print('You got A grade!')

    elif num <= 89 and num >= 80:
        print('You got B grade!')

    elif num <= 79 and num >= 70:
        print('You got C grade!')

    elif num <= 69 and num >= 60:
        print('You got D grade!')

    else:
        print('You got F grade!')


main()
