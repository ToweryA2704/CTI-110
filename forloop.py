# get numnber of values to sum

num_count = int(input("Enter the numebr of values to add: "))

# initialize the total accumulator
total = 0

# For loop to get numbers to add up

for i in range(num_count):
    num = float(input("Enter a number: "))
    total = num + total
    #total += num
print("Total:", total)
