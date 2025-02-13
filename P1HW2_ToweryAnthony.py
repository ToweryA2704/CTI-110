 # Anthony Towery
 # February 11th, 2025
 # P1HW2
 # A Python program that uses budget calculations and travel expenses.

print("This program calculates and displays travel expenses")
budget = int(input("\nEnter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = int(input("\nHow much do you think you will spend on gas? "))
accomodation = int(input("\nApproximately, how much will you need for accomodation/hotel? "))
food = int(input("\nLast, how much do you need for food? "))
print("\n------------Travel Expenses------------")
print("Location:",destination)
print("Initial Budget:",budget)
print("\nFuel:",gas)
print("Accomodation:",accomodation)
print("Food:",food)
# calculation
balance = budget-gas-accomodation-food
print("\nRemaining Balance:",balance)

##Pseudocode
##Ask user to enter their budget
##Ask user to enter travel destination
##Ask user for amount they will spend on gas
##Ask user for amount they will spend on accommodation
##Ask user for amount they will spend on food
##Add expenses
##Subtract expenses from budget
##Display results
