''' Sunny Dhindsa sd3692
CSCI.0002-004 Dakota Hernandez Mon/Wed 3:30-4:45
Assignment 2, problem 2 due 9/22/19
'''
#create a pizza ordering program which charges for ordering different size pizzas

#store prices of each size of pizza
small = 11.95
medium = 14.95
large = 17.95

#ask user for their name and greet user
name = input("To start, what is your name? ")
print("Hello, ", name , "!", sep = "")

#ask how many pizzas they would like for each type
smallOrder = float(input("How many small pizzas would you like? "))
mediumOrder = float(input("How many medium pizzas would you like? "))
largeOrder = float(input("How many large pizzas would you like? "))

#thank user for their order
print("Thank you for your order,", name, ".")

#create variables to calculate price for order. make sure to format to 2 decimal places
smallCalc = smallOrder*small
mediumCalc = mediumOrder*medium
largeCalc = largeOrder*large

#create variable for total calculation, formatting to 2 decimal points

totalCalc = format(smallCalc+mediumCalc+largeCalc, '.2f')

#print total price

print("Your total price is $", totalCalc , ". Have a nice day!", sep="")



