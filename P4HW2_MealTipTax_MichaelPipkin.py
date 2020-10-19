#Calculates the total amount of a meal purchased at a restaurant
#09/24/2020
#CTI-110 P2HW1 - Meal Tip Tax Calculator
#Michael Pipkin II

num1 = float(input('Enter food cost: '))
num2 = float(input('Enter tip amount of 15, 18, or 20: '))

#validating tip percentage
if (num2 == 15):
    print('15%')

elif(num2 == 18):
    print('18%')

elif(num2 == 20):
    print('20%')

else:
    print("Invalid! Please enter tip again!")

#assigning tax as 6 percent
num3 = 6.0

#calculating tip amount
num4 = num1 *(num2/100)

#calculating tax amount
num5 = num1 *(num3/100)

#printing the results
print("Calculated Tip: %.2f"%(num4))
print("Calculated Tax: %.2f"%(num5))
print("Total cost including tip and tax: %.2f"%(num1+num4+num5))
