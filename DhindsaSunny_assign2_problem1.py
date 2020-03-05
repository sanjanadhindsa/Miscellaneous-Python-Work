'''Sunny Dhindsa sd3692
CSCI.0002-004
Assigment 2, problem 1 due 22 September 2019
'''
#calculate tip. needs to accept how much total bill is and how much tip to leave
print("Hello! I'm here to help you calculate your tip.")

#create variable to ask how much the bill is
bill = float(input("How much was your bill? Enter just a number: " ))

#create variable to ask the user how much to tip.

tip = float(input("How much would you like to tip?: "))
print("Thanks!")

#create variables to calculate tip and bill total. Format to 2 decimal points
tipTotal = float(format(bill*tip/100, '.2f'))
billTotal = float(format(tipTotal + bill, '.2f'))

#have program tell user how much to tip
print("You need to leave $", tipTotal, " as a tip", sep="")
#have program tell user their total bill
print("Your total bill will be $", billTotal, sep = "")


