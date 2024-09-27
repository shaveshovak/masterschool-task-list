# Write a Python script that
# 1. continuously prompts the user to enter a positive integer.
# 2. If the user enters an invalid value (e.g., a negative number or a non-integer), the script should inform the user and ask them to try again.
# 3. The loop should continue until the user provides a valid positive integer.


while True:
    user_input = input("Enter a positive number: ")

    try:
        number = int(user_input)
        if number > 0:
            print(f"The number {number} is positive.")
            break
        else:
            print(f"The number {number} is negative. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a positive number.")





