class BankAccount:
    def set_details(self, name, balance = 0):
      self.name = name
      self.balance = balance

    def display(self):
       print(self.name, self.balance)

    def withdraw(self, amount):
       self.balance -= amount 

    def deposit(self, amount):
         self.balance += amount


x = BankAccount()
y = BankAccount()


x.set_details('Account_01', 10000)
y.set_details('Account_02', 15000)

x.deposit(2500)
y.withdraw(2500)

x.display()
y.display()