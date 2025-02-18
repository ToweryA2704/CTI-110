# This shows pi and math in Python
import math
x = math.pi
print("The value of pi in the math function is", x)
# two ways to format the pi value
# first way
# format(variable name ,',2f')
# print(x)
print("The value of pi in the math function is",format(x,',.2f'),'.')
print("The value of pi in the math function is " + str(format(x,',.2f')+'.'))

# 2nd way

#print(f' ')
print(f'The value of pi in the math function is {x}.')
print(f'The value of pi in the math function is {x:,.4f}.')

num1 = 5.5
num2 = 6.7

num3 = math.pow(num1, num2)
print(num1,"to the power of", num2, "equals", num3,".")
print(f'{num1:5.2f} to the power of {num2:5.2f} equals {num3:25,.2f}.')

##num4 = math.sqrt(num3) * math.sqrt(num3)
##
##print(num4)
