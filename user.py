
class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):	
    	self.account_balance += amount

    def make_withdrawal(self,amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

andrew = User("Andrew Shaw", "andrew@python.com")
andrew.make_deposit(50)
andrew.make_deposit(50)
andrew.make_deposit(50)
andrew.make_withdrawal(50)
andrew.display_user_balance()
james = User("James Wongsudin", "james@python.com")
james.make_deposit(100)
james.make_deposit(100)
james.make_withdrawal(50)
james.make_withdrawal(50)
james.display_user_balance()
mason = User("Mason Holland", "mason@python.com")
mason.make_deposit(250)
mason.make_withdrawal(50)
mason.make_withdrawal(50)
mason.make_withdrawal(50)
mason.display_user_balance()
