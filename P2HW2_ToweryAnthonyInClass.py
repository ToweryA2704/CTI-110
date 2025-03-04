 # Anthony Towery

 # March 4th, 2025

 # P2HW2

 #Brief description of program

mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))
gradeList = [] # empty list
gradeList = [mod1, mod2, mod3, mod4, mod5, mod6] # add variables to the list
print(gradeList)

##gradeList = [] # empty list
##mod1 = float(input("Enter grade for Module 1: "))
##gradeList.append(mod1)
##mod1 = float(input("Enter grade for Module 2: "))
##gradeList.append(mod1)
##mod1 = float(input("Enter grade for Module 3: "))
##gradeList.append(mod1)
##mod1 = float(input("Enter grade for Module 4: "))
##gradeList.append(mod1)
##mod1 = float(input("Enter grade for Module 5: "))
##gradeList.append(mod1)
##mod1 = float(input("Enter grade for Module 6: "))
##gradeList.append(mod1)
##print(gradeList)
##gradeList.sort()
##gradeList.reverse()
##print(*gradeList)
##(gradeList[1])


# figure out the lowest, highest, sum, and the length
lowest = min(gradeList)
highest = max(gradeList)
total = sum(gradeList)
average = total / len(gradeList)

#print the results
print("\n ------------Results------------")
print(f"Lowest Grade: {lowest}")
print(f"Highest Grade: {highest}")
print(f"Sum of Grades: {total}")
print(f"Average: {average:.2f}")
print('-'*32)