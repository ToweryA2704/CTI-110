# Anthony Towery
# February 27th, 2025
# P2HW2
# Showing a list of grades

import statistics

# Ask user to import their test grades
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))


# Store info on a list
grades = list["module1", "module2", "module3", "module4", "module5", "module6"]

lowestgrade = min({module1, module2, module3, module4, module5, module6})
highestgrade = max({module1, module2, module3, module4, module5, module6})
alltogether = sum({module1, module2, module3, module4, module5, module6})
#adverage = statistics.mean({module1, module2, module3, module4, module5, module6})

print("\n ------------Results------------")
print(f"Lowest Grade: {lowestgrade}")
print(f"Highest Grade: {highestgrade}")
print(f"Sum of Grades: {alltogether}")
print(f"Average: {adverage:.2f}")
print("----------------------------------------")
# Pseudocode
# Ask user to enter their grade for each module
#
