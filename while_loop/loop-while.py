# First explanation
i = 0
while i < 50:
    print(i)
    break 

# Second explanation, if we want to show the numbers until 50, loop until 50 
i = 0
while i < 50:
    print(i)
    i += 1 

#3
i = 0
while i < 50:
    print(i)
    i += 1 
else: #else will be executed when there is no break 
    print('done with all work')

#4
mylist = [1, 2, 3]
# When do we use while loop 
i = 0
while i < len(mylist):
    print(mylist[i])
    i+=1

# When do we use for loop
for item in mylist:
    print(item)

# Infinite Loop 
while True: 
    response = input('Say something')
    if(response == 'bye'):
        break

# Write a Python script that
# 1. continuously prompts the user to enter a positive integer. 
# 2. If the user enters an invalid value (e.g., a negative number or a non-integer), the script should inform the user and ask them to try again. 
# 3. The loop should continue until the user provides a valid positive integer.

while True:
    # Infinite Loop (while True): The while True statement creates an infinite loop. This loop will continue running until it is explicitly broken out of with a break statement.
    user_input = input("Please enter a positive integer: ")
    # User Input (input()): The input function prompts the user to enter a value and stores it in the variable user_input.
    try:
        number = int(user_input)
        if number > 0:
            print(f"Thank you! You entered a positive integer: {number}")
            break
        else:
            print("That's not a positive integer. Please try again.")
    except ValueError:
        # If a ValueError occurs (i.e., if the user input cannot be converted to an integer), the script prints an error message indicating that the input was invalid and prompts the user to enter a valid integer again.
        print("Invalid input. Please enter a valid integer.")

    # The try block attempts to convert the user_input to an integer using int(user_input). If this succeeds, the value is stored in the variable number.
    # If the conversion fails (e.g., if the user input is not a valid integer), a ValueError is raised, and the code moves to the except block. 
