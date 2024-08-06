# class BankAccount:
#     def __init__(self, account_holder, balance=0.0):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{self.account_holder} - Deposited ${amount}. New balance: ${self.balance}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds!")
#         else:
#             self.balance -= amount
#             print(f"{self.account_holder} - Withdrew ${amount}. New balance: ${self.balance}")

#     def get_balance(self):
#         return self.balance

#     def __str__(self):
#         return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"


# # Example usage of the BankAccount class
# # if _name_ == "__main__":
#     # Creating accounts
# ramuAccount = BankAccount("Ramu")
# somuAccount = BankAccount("Somu", 1000.0)

#     # Performing transactions
# ramuAccount.deposit(500.0)
# somuAccount.withdraw(200.0)

#     # Displaying account information
# print(ramuAccount)
# print(somuAccount)

class BankAccount:
    def __init__(self,account_holder,balance=0.0):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amt):
        self.balance+=amt
        print(f"{self.account_holder} - Deposit ${amt} - New Balance ${self.balance}")
    def witdraw(self,amt):
        if amt>self.balance:
            print("Insufficient Balance")
        else:
            self.balance-=amt
            print(f"${self.account_holder} - WithDrew ${amt} - New Balance - ${self.balance}")
    def getBalance(self):
        print(f"${self.account_holder} - Balance ${self.balance}")
    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"
        
        
ramuAccount=BankAccount("Ramu",1000)
ramuAccount.deposit(1000)
# ramuAccount.witdraw(300)
# ramuAccount.getBalance()
print(ramuAccount)