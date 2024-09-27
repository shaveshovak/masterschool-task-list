# Task 1 
# Improve Code Styling: Ensure proper indentation and spacing.
# Add Documentation: Write a docstring for the function.
# Use Constants: Define π (pi) as a constant.

def calcArea(r):
    pi = 3.14159
    return pi * r * r

radius = 5
area = calcArea(radius)
print("Area:", area)

# Task 2
# Rename Variables: Use more descriptive names.
# Improve Readability: Add type hints and a docstring.
# Use Constants: If applicable, identify any magic numbers and define them as constants.

def c(lst):
    total = 0
    for i in lst:
        total += i
    return total

nums = [1, 2, 3, 4, 5]
print("Sum:", c(nums))

# Task 3
# Use Constants: Define the conversion factors as constants.
# Add Documentation: Write a docstring for the function.
# Improve Naming: Use descriptive variable names and type hints.

def convert_temp(celsius):
    return celsius * 9/5 + 32

temp_c = 30
temp_f = convert_temp(temp_c)
print("Temperature in Fahrenheit:", temp_f)
