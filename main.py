from user import User
from bank import Bank


tommy = User('Tommy', 33, 'Male')
tim = User('Tim', 22, 'Male')
john = Bank('John', 28, 'Male')

john.deposit(100)
john.deposit(10)
john.withdraw(60)
john.view_balance()


