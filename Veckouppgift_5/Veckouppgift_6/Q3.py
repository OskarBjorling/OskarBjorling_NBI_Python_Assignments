class bank_account:
    def __init__(self, name, balance=0):
        self.account_name = name
        self.balance=balance
        self.roundedbalance=round(balance,2)
        self.print_info(" efter upprättande")

    def deposit(self,amount=0):
        self.balance+=amount
        self.print_info(f" efter insättning av {amount} kr")

    def withdraw(self,amount=0):
        if self.balance>=amount:
            self.balance-=amount
            self.print_info(f" efter uttag av {amount} kr")
        else:
            self.print_info(f". Uttag av {amount} kr nekas")


    def check_balance(self):
        return self.balance
        self.print_info()

    def add_interest(self, rate=0, days = 0):
        interest= (self.balance * rate * days / (365 * 100))
        self.balance += interest
        self.print_info(f". {interest} kr ränta har ackumulerats efter {days} dagar med {rate}% ränta")

    def print_info(self, text=""):
        print(f"Kontot {self.account_name} innehåller {self.balance} kr{text}")

def test_account(account):
    assert account.account_name == "TestAccount"
    assert account.balance == 0
    account.deposit(1000)
    assert account.balance == 1000
    account.withdraw(1000)
    assert account.balance == 0
    account.withdraw(1000)
    assert account.balance == 0
    account.deposit(1000)
    assert account.balance == 1000
    account.add_interest(100,365)
    assert account.balance == 2000

name = "NBI"
rate = 0.03
balance = 10000
deposit = 1000
withdraw = 500

account = bank_account(name, 10000)
account.deposit(1000)
account.withdraw(20000)
account.add_interest(10,365)
account.check_balance()

account = bank_account("TestAccount", 0)
test_account(account)
