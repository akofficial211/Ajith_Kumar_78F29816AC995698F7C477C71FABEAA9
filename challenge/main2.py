#Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality.
class BankAccount:
    def _init_(self, acc_number, acc_holder_name, initial_balance):
        self.__account_number = acc_number
        self.__account_holder_name = acc_holder_name
        self.__account_balance = initial_balance
    
    def deposit(self, amount):
        self.__account_balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient funds")
    
    def display_balance(self):
        return self.__account_balance

# Creating an instance of the BankAccount class
my_account = BankAccount("123456789", "John Doe", 1000)

# Testing deposit and withdrawal functionality
my_account.deposit(500)
my_account.withdraw(200)
balance = my_account.display_balance()

print(f"Account Holder: {my_account.BankAccount_account_holder_name}")
print(f"Account Number: {my_account.BankAccount_account_number}")
print(f"Account Balance: {balance}")