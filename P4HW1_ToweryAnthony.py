# Anthony Towery

# March 27th, 2025

# P4HW1

# Improving the P2HW2 assignment with loops

# This program takes a number grade , determines average and displays letter grade for average.

# Store info on a list
scoreList = []
# Ask user to import their scores
num = int(input("How many scores do you want to enter: "))
print("\n")
for i in range(1,num+1):
    score = float(input(f'Enter score #{i}: '))
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f'Enter score #{i} again: '))  
    scoreList.insert(i-1, score)
#print(scoreList)

#gradeList = [module1, module2, module3, module4, module5, module6] # add variables to the list

# figure out the lowest, list, sum, and the average
lowest = min(scoreList)
scoreList.remove(lowest)
total = sum(scoreList)
average = total / len(scoreList)

#print the results
print("\n ------------Results------------")
print(f'{"Lowest Score ":<15} : {lowest}')
print(f'{"Modified List ":<15} : {scoreList}')
print(f'{"Scores Average ":<15} : {average:.2f}')
if average >= 90:
    print('Grade           : A')
else:
    if average >= 80:
        print('Grade           : B')
    else:
        if average >= 70:
            print('Grade           : C')
        else:
            if average >= 60:
                print('Grade           : D')
            else:
                print('Grade           : F')
print('-'*40)
