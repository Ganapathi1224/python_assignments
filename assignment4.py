class AutomatedTellerMachine:
     
    def card_insertion(password,enteredpassword):
        if(password==enteredpassword):
           print("\ncorrect password")
        else:
           print("\nwrong password")
    card_insertion(2,2)

    print("\nplease! do not remove the card,during the entire transaction\n")

    def __init__(self,balance,withdraw ):
        self.balance=balance
        self.withdraw=withdraw

    def inquiry (self):
        return f"current balance in your account is {self.balance}"
    
    def withdrawal_amount(self):
        if(self.balance<self.withdraw):
            return "Transaction failed!\nLOW BALANCE!!"
            
        else:
            return f"withdrawal amount is {self.withdraw}"
        
    print("cash can be withdrew sucessfully")

    def after_withdrawal(self):
        newbalance=self.balance-self.withdraw
        self.newbalance=newbalance
        return f"After withdrawal:\n\nthe account balance is {self.newbalance}"
    
    def deposit_amount(self,deposit):
        return f"After deposit:\n\nthe account balance is {self.newbalance+deposit}\n"
    

    
obj1=AutomatedTellerMachine(200,150)
print(obj1.inquiry(),"\n")
print(obj1.withdrawal_amount(),"\n")
print(obj1.after_withdrawal(),"\n")
print(obj1.deposit_amount(200))



#MatchCase
class BankDetails:

    def bank_name():
        bank="HDFC"
        match bank:
            case "Indian":
                print("your bank name is Indian")
            case "HDFC":
                print("your bank name is HDFC\n")
            case "Axis":
                print("your bank name is Axis")
            case "canara":
                print("your bank name is canara")
            case _:
                print("You does not have any bank account")
    bank_name()

    def branch_name(branch):
        match branch:
            case "vellore":
                print("your branch name is Vellore")
            case "Sipcot":
                print("your branch name is Sipcot")
            case "Ranipet":
                print("your branch name is Ranipet\n")
            case "Arcot":
                print("your branch name is Arcot")
            case _:
                print("your branch could not be find")
    branch_name("Ranipet")



#ExceptionHandling
class AccountDetails:

    def account_number():
        try:
            number=int(input("Enter the account number="))
            print("your account number is ",number)
        except ValueError:
            print("\nplease, enter the number\n\nDo not enter the  letter or word")
        except:
            print("Invalid input")
    account_number()

    def account_type():
        acctype=["current","saving"]
        try:
            print("\nyour account is ",acctype[2])
        except IndexError:
            print("\nindex value of the acctype is out of range\n \nplease, enter within th index range")
        except:
            print("\nInvalid input ,ERROR OCCURED!!!")
    account_type()


"""
OUTPUT:

correct password

please! do not remove the card,during the entire transaction

cash can be withdrew sucessfully
current balance in your account is 200

withdrawal amount is 150

After withdrawal:

the account balance is 50

After deposit:

the account balance is 250

your bank name is HDFC

your branch name is Ranipet

Enter the account number=dffgfdgkl

please, enter the number

Do not enter the  letter or word

index value of the acctype is out of range

please, enter within th index range

"""

