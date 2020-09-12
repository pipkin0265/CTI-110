#Using IDLE to create and test code
#09/11/2020
#CTI-110 P1HW2 - Basic Math
#Michael Pipkin

print('Please Enter First Number:', end=' ')    #Ask user to enter first number
first_num = input()

print('Please Enter Second Number:', end=' ')   #Asks user to enter second number
second_num = input()

print(end='\n')                                 #Newline character

print('First Number Entered:', first_num)       #Prints number enetered
print('Second Number Entered:', second_num)     #Prints second number entered

print(end='\n')                                 

sum = (int(first_num) + int(second_num))        #The sum of the first and second numbers entered
print('Sum of Both Numbers:', sum, end='\n')

prod = (int(first_num) * int(second_num))       #The multiplication of the first and second numbers entered
print('Result of Multiplying The Two Numbers:', prod, end=' ')
