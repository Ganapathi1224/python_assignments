class MoneyTransaction:
    def __init__(self,balance,withdraw ):
        self.balance=balance
        self.withdraw=withdraw

    def current_balance(self):
        return self.balance
    def withdrawal_amount(self):
        if(self.balance<self.withdraw):
            return "Transaction failed!\nLOW BALANCE!!"
            
        else:
            return self.withdraw
    def after_withdrawal(self):
        return self.balance-self.withdraw
    def deposit_amount(self,deposit):
        return self.balance-self.withdraw+deposit

   
obj1=MoneyTransaction(200,150)
print("current balance in your account is ",obj1.current_balance(),"\n")
print("withdrawal amount is ",obj1.withdrawal_amount(),"\n")
print("After withdrawal\nnow the current account balance is ",obj1.after_withdrawal(),"\n")
print("after deposit\nthe account balance is ",obj1.deposit_amount(200))

''' 
 OUTPUT:
current balance in your account is  200

withdrawal amount is  150

After withdrawal
now the current account balance is  50

after deposit
the account balance is  250
'''        