# Anthony Towery
# March 25th, 2025
# P4LAB2
# Make a program that uses while and for loop.

keep_going = 'yes'
while keep_going.lower() == 'yes':
    num = int(input("\nEnter an integer: "))
    while num < 0 or num > 12:
        print("\nInvalid Entry!")
        print("\nInteger must be greater or equal to 0 and less than 13\n")
        if num < 0:
            print("This program does not handle negative values\n")
            # Added that in on line 13 so that it knows that it cannot handle negative numbers since the bottom print code at line 22 wouldn't work
        num = int(input("Enter an integer: "))
    print("\n")
    if(num >= 0):
        for i in range(1,12+1):
            print(f'{num} * {i} = {num * i}')
        print("\n")
    #else:
    #    print("This program does not handle negative values")
    #print("\n")
    keep_going = input("Do you want to enter more numbers? Enter yes or no: ")
print("\nExiting the program...")