class charity_fund:
    def __init__(self,balance=1000000):
        self.balance = balance

    def save_fund(self,amount):
        self.balance += amount
    
    def spend_fund(self,amount):
        self.balance -= amount
    
    def invest_fund(self,retun_rate):
        self.balance *= 1 + retun_rate

    def get_balance(self):
        if self.balance < 0:
            print('You got a deficit of ' + str(-self.balance))
        return self.balance

    def is_danger(self):
        if self.balance < 50000:
            print('Danger. You have ' + str(self.balance) + 'Left')
        return self.balance < 50000

help_elderly = charity_fund()
help_elderly.spend_fund(200000)
print(help_elderly.get_balance())
help_elderly.invest_fund(-0.05)
print(help_elderly.get_balance())
help_elderly.save_fund(100000)
print(help_elderly.get_balance())
help_elderly.spend_fund(900000)
print(help_elderly.get_balance())
print(help_elderly.is_danger())