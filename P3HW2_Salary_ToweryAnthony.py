# Anthony Towery
# March 18, 2025
# P3HW2
# Program shows employee information and hours and pay

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employee's pay rate: "))
print('-'*37)
print(f"{"Employee name:":<15} {name}")
print()

if hours > 40:
    reg_pay = 40 * rate
    ovt_hrs = hours - 40
    ovt_pay = ovt_hrs * rate * 1.5
    gross_pay = ovt_pay + reg_pay
else:
    reg_pay = hours * rate
    ovt_hrs = 0
    ovt_pay = 0
    gross_pay = ovt_pay + reg_pay

print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay":<12}')
print('-'*102)
print(f'{hours:<15.1f}{rate:<12.1f}{ovt_hrs:<12.1f}{ovt_pay:<20.2f}{"$"}{reg_pay:<20.2f}{"$"}{gross_pay:<12.2f}')