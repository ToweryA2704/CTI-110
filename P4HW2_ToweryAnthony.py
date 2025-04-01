# Anthony Towery
# April 1, 2025
# P4HW2
# Improving P3HW2 by adding a loop for multiple employees and return a total payment

#request employee information
name = input("Enter employee's name or \"Done\" to terminate: ")
overTime_total = 0
regPay_total = 0
gross_total = 0
Employee_count = 0
while name !="Done":
    #add one to Employee_count var
    Employee_count +=1
    #ask for employee information
    hoursWorked = float(input("How many hours did "+name+" work? "))
    payRate = float(input("What is "+name+"'s pay rate? "))
    #evalute overtime
    if hoursWorked >40:
        #print("regular pay")
        reg_pay = 40 * payRate
        ovt_hrs = hoursWorked - 40
        overPay = ovt_hrs * payRate * 1.5
        gross_pay = overPay + reg_pay
    else:
        #print("over time pay")
        reg_pay = hoursWorked * payRate
        ovt_hrs = 0
        overPay = 0
        gross_pay = overPay + reg_pay
#display output
    print("\nEmployee name: ",name,"\n")
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
    print("-----------------------------------------------------------------------------------------")
    print(f'{hoursWorked:<15}{payRate:<12.2f}{ovt_hrs:<12.1f}{overPay:<20.2f}{"$"}{reg_pay:<20.2f}{"$"}{gross_pay:<.2f}')
    print()
#ask user for another employee name
    name = input("\nEnter employee's name or \"Done\" to terminate: ")
    overTime_total = overTime_total + overPay
    regPay_total = regPay_total + reg_pay
    gross_total = gross_total + gross_pay
    print()
#display final results
#display overtime total, regular pay total, gross pay total and number of employees entered
print("\nTotal number of employees entered: ",Employee_count, sep="")
print("Total amount paid for overtime: $", format(overTime_total,".2f"), sep="")
print("Total amount paid for regular hours: $", format(regPay_total,".2f"), sep="")
print("Total amount paid in gross: $", format(gross_total,".2f"), sep="")