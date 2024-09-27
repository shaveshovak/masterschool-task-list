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

# Solution 
# Define a constant for π (pi)
PI = 3.14159

def calc_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    return PI * radius * radius

if __name__ == "__main__":
    radius = 5
    area = calc_area(radius)
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

# Solution 
def calculate_sum(numbers: list[int]) -> int:
    """
    Calculate the sum of a list of numbers.
    
    Parameters:
    numbers (list[int]): A list of integers.
    
    Returns:
    int: The sum of the numbers in the list.
    """
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("Sum:", calculate_sum(numbers))


# Task 3
# Use Constants: Define the conversion factors as constants.
# Add Documentation: Write a docstring for the function.
# Improve Naming: Use descriptive variable names and type hints.

def convert_temp(celsius):
    return celsius * 9/5 + 32

temp_c = 30
temp_f = convert_temp(temp_c)
print("Temperature in Fahrenheit:", temp_f)

# Solution 

FACTOR = 9 / 5
OFFSET = 32

def convert_to_fahrenheit(celsius: float) -> float:
    """
    Convert a temperature from Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): The temperature in Celsius.
    
    Returns:
    float: The temperature in Fahrenheit.
    """
    return celsius * FACTOR + OFFSET

if __name__ == "__main__":
    temperature_celsius = 30
    temperature_fahrenheit = convert_to_fahrenheit(temperature_celsius)
    print("Temperature in Fahrenheit:", temperature_fahrenheit)
