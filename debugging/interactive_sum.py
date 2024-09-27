def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def sum_two_numbers(a, b):
    return a + b


def main():
    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        result = sum_two_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}")

        continue_input = input("Do you want to enter another set of numbers? (yes/no): ")
        if continue_input.lower() != 'yes':
            break


main()

# input(prompt) displays the prompt to the user and waits for input
# int(input(prompt)) attempts to convert the input to an integer
# If the conversion fails (i.e., the input is not a valid integer), a ValueError is raised
# The except ValueError block catches this exception and prints an error message

# It contains an infinite loop (while True) that continues to execute until the user decides to stop
