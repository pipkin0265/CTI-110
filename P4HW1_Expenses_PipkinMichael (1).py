#CTI-110
#P4HW1 - Expenses
#Michael Pipkin II
#10/17/2020

#Accumulator
account_balance = 0
ending_balance = 0
expense = 0
keep_going = "y"

#Prompt user for account balance.
account_balance = float(input("Enter starting amount in account: $"))

#Ending balance set to be starting balance at the beginning
ending_balance = account_balance

#Calculate the balance
for a in range (1000):
    while keep_going == "y":

        #prompt user for expense
        purchase = int(input("Enter expense: "))

        #update the ending balance
        ending_balance = ending_balance - purchase

        #calculate total expenses
        expense = expense + 1

        #Ask if there is another expense
        keep_going = input("Do you want to enter another expense? (y/n)")

if keep_going == "n":
    print("Amount in account before expenses subtraction $", format (account_balance, ",.2f"))
    print("Number of expense entered:", expense)
    print("Amount in account AFTER expenses subtracted is $", format (ending_balance, ",.2f"))

        
