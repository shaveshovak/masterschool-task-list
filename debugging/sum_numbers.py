def sum_numbers(numbers):
    return sum(numbers)


def main():
    numbers_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, numbers_input.split()))
    result = sum_numbers(numbers)
    print(f"The sum of the numbers is: {result}")


main()

# The input function displays the prompt "Enter numbers separated by spaces: " and waits for the user to type a
# response and press Enter. The user's input is captured as a string and stored in the variable numbers_input.
# Example: If the user types 1 2 3 4 5, then numbers_input will be the string "1 2 3 4 5"


# The split() method splits the string numbers_input into a list of substrings based on whitespace by default.
# Example: "1 2 3 4 5".split() results in the list ["1", "2", "3", "4", "5"].

# map(int, numbers_input.split()): The map function applies the int function to each element of the list obtained
# from split(), converting each substring to an integer. Example: map(int, ["1", "2", "3", "4", "5"]) results in a
# map object containing the integers 1, 2, 3, 4, 5.

# list(map(int, numbers_input.split())):
# The list function converts the map object to a list of integers.
# Example: list(map(int, ["1", "2", "3", "4", "5"])) results in the list [1, 2, 3, 4, 5].
