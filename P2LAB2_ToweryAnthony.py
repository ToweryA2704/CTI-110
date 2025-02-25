# Anthony Towery

# February 25th, 2025

# P2LAB2

# Creating a dictionary with some key-value pairs

# create dictionary
cars ={
    "Camaro": 18.21,
    "Prius" : 52.36,
    "Model S" : 110,
    "Silverado" : 26
    }
# Display Results of all keys in dictionary

keys = cars.keys()
print(keys)
print()
car_input = input("Enter a vehicle to see it's mpg: ")
print()
mpg_output = cars[car_input]
# Display output
print(f'The {car_input} gets {mpg_output} mpg. \n')
