
# Define the BankAccount class
class BankAccount:
    # Initialize the account with account number and initial balance
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number  # Unique identifier for the account
        self.balance = initial_balance  # Starting balance of the account

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Add amount to the current balance
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount  # Subtract amount from the current balance
            print(f"Withdrawn: ${amount}")
        else:
            print("Insufficient funds.")

    # Method to get the current balance of the account
    def get_balance(self):
        return self.balance


# Create an instance of the BankAccount class
# Account number: 12345, Initial balance: $1000
account = BankAccount(12345, 1000)

# Perform operations
print(f"Initial balance: ${account.get_balance()}")

# Deposit $500 into the account
account.deposit(500)

# Withdraw $300 from the account
account.withdraw(300)

# Check the final balance after the transactions
print(f"Final balance: ${account.get_balance()}")


# Attributes:
    # account_number: A unique identifier for each account.
    # balance: Represents the current balance in the account.
# Methods:
    # __init__(self, account_number, initial_balance): Initializes a new bank account with the given account number and balance.
    # deposit(self, amount): Adds money to the balance.
    # withdraw(self, amount): Subtracts money from the balance if there are sufficient funds.
    # get_balance(self): Returns the current balance.