from user import User

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print('Account balance has been updated !')
        print('Account balance is: $', self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient balance !')
            print('Available  balance: $', self.balance)
        else:
            self.balance -= amount
            print('Account balance has been updated !')
            print('Account balance is: $', self.balance)

    def view_balance(self):
        self.show_details()
        print('Account balance is: $', self.balance)
        