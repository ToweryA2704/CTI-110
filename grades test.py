def main():
    #call all the other functions
    number = getNumGrades()
    total = getGradesTotal(number)
    average = getAverage(number, total)
    grades = getLetterGrade(average)
    displayGrades(average, grades
def getNumGrades():
    num = int(input("How many grades do you want to input? "))
    return num
def getGradesTotal(num):
        total = 0
        for x in range (num):
             grade = float(input("Enter a grade "))
             total = grade + total
        return total
def getAverage(num, total):
     ave = total / num
     return ave
    #return total / num
def getLetterGrade(ave):
    if ave >= 90:
        grade = "A"
    elif ave >= 80:
        grade = "B"
    elif ave >= 70:
        grade = "C"
    elif ave >= 60:
        grade = "D"
    else:
     grade = "F"
    return grade
def displayGrades(ave, grade):
    print("Your average is ", ave, " which is letter grade of ", grade)
main()