
class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):	
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

andrew = User("Andrew Shaw", "andrew@python.com")
andrew.make_deposit(50).make_deposit(50).make_deposit(50).make_withdrawal(50).display_user_balance()
james = User("James Wongsudin", "james@python.com")
james.make_deposit(100).make_deposit(100).make_withdrawal(50).make_withdrawal(50).display_user_balance()
mason = User("Mason Holland", "mason@python.com")
mason.make_deposit(250).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()
