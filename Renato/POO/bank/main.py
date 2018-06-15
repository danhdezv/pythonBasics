''' 
  BankAccount

'''

class BankAccount:
  def __init__(self):
    self.balance = 0

  def deposit(self, amount):
    self.balance = self.balance + amount # equalTo: self.balance += amount 
    return self.balance

  def withdraw(self, amount):
    self.balance -= amount
    return self.balance

bankAccount1 = BankAccount()
amount = input('ingresa el primer deposito ')
bankAccount1.deposit(int(amount)) 
print(bankAccount1.balance)
