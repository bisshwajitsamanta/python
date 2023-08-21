class Account:
    def __init__(self, account_number: str, account_type: str, initial_balance: int):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f'Deposited: {amount}')
            print(f'New Balance is : {self.balance}')
        else:
            print(f'{amount} is an invalid amount')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance = self.balance - amount
            print(f'Withdrawl: {amount}')
            print(f'New Balance : {self.balance}')
        else:
            if amount < 0:
                print(f'{amount} is an invalid amount')
            else:
                print("Insufficient Funds")
                print(f'Current Balance is {self.balance}')


my_account = Account('123-456', 'Savings',10_00)
print(f'Account Number {my_account.account_number}')
print(f'Account Number {my_account.balance}')
my_account.deposit(100)
my_account.withdraw(20)
my_account.withdraw(20_000)
