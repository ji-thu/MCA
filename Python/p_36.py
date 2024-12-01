
class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0.0):
       
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
            print "Deposited {0}. \nNew balance: {1}".format(amount, self.balance)
        else:
            print "Deposit amount must be positive."

    def withdraw(self, amount):
        
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print "Withdraw {0}. \nNew balance: {1}".format(amount, self.balance)
            else:
                print "Insufficient balance for withdrawal."
        else:
            print "Withdrawal amount must be positive."

    def get_balance(self):
        
        return self.balance

    def account_details(self):
       
        return "Account Number: {0}\nName: {1}\nAccount Type: {2}\nBalance: {3}".format(self.account_number, self.name, self.account_type, self.balance)

account_number=int(raw_input("Enter your account number:"))
name=raw_input("Enter name:")
account_type=raw_input("Enter account type")
balance=0.0
account1 = BankAccount(account_number, name, account_type, balance)

 
print account1.account_details()

deposit=int(raw_input("Enter the amount you want to deposit:"))
account1.deposit(deposit)

withdraw=int(raw_input("Enter the amount you want to withdraw:")) 
account1.withdraw(withdraw)

 
print "Updated Balance:", account1.get_balance()
