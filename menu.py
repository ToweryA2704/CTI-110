choice = 'y'
while(choice.lower() == 'y'):
    #print menu
    print()
    print("Menu")
    print("1. Program 1")
    print("2. Program 2")
    print("3. Program 3")
    print("4. Exit the Program\n")
    #choice = input("Do you want to run the program again? Enter y/n: ")
    value = int(input("Please enter your choice: "))
    # get choice option
    if value == 1:
        print("\nYou picked option 1")
        print()
    elif value == 2:
        print("\nYou picked option 2")
        print()
    elif value == 3:
        print("\nYou picked option 3")
        print()
    elif value == 4:
        print("\nYou picked option 4")
        print("Exiting the program")
        print("Goodbye")
        print()
        choice = 'n'
    else:
        print("Invalid choice. Please choose a valid option!")
        input("Press any key to continue: ")
    #print("Exiting the program!")