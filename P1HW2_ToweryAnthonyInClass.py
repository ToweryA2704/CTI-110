 # Anthony Towery
 # February 13th, 2025
 # P1HW2
 # A Python program that uses budget calculations and travel expenses.

print("This program calculates and displays travel expenses\n")
budget = int(input("Enter Budget: "))
print()
location = str(input("Enter your travel destination: "))
print()
gas = int(input("How much do you think you will spin on gas? "))
print()
lodging = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
print()

print("-"*12,"Travel Expenses","-"*12)
print("Location: ",location)

# calculation
balance = budget - gas - lodging - food
print("Remaining Balance: ", balance)
#print("Remaing Balance: ",budget - (gas + lodging + food))
##Pseudocode
##Ask user to enter their budget
##Ask user to enter travel destination
##Ask user for amount they will spend on gas
##Ask user for amount they will spend on accommodation
##Ask user for amount they will spend on food
##Add expenses
##Subtract expenses from budget
##Display results

