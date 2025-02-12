#Encapsulation

class BankAccount:
    """A class with private attributes for security."""

    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private variable
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return f"New Balance: {self.__balance}"

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        return f"New Balance: {self.__balance}"


# Creating an account
account = BankAccount("123456", 1000)

# Depositing money
print(account.deposit(500))  # Output: New Balance: 1500

# Trying to access private variable (Will cause error)
# print(account.__balance)
