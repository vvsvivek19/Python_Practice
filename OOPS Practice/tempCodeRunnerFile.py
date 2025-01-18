#SOLUTION 3
starting_acc_num = 1000
class BankAccount:
    def __init__(self,acc_num=None,acc_holder=None,bal=500):
        self.account_number = acc_num
        self.account_holder = acc_holder
        self.balance = bal
        self.create_account()
    def create_account(self):
        global starting_acc_num
        self.account_number = starting_acc_num
        starting_acc_num += 1
        self.account_holder = input("Please Enter the account holder name:")
        print("Account created successfully with minimum balance 500!!")
    def deposite(self,amount):
        self.balance = self.balance + amount
    def withdraw(self,amount):
        if self.balance - amount < 0:
            print("Minimum balance cannot be less than zero!")
        else:
            self.balance = self.balance - amount
    def account_details(self):
        print("Printing account holder's details")
        print("*********************************")
        print("Account Number:",self.account_number)
        print("Account Holder:",self.account_holder)
        print("Balance:",self.balance)
    def menu(self):
        print("Welcome to United Bank, Please choose from below:")
        print("1. Print account details")
        print("2. Deposite Money")
        print("3. Withdraw money")
        print("4. Exit")
        choice = int(input("Please Enter the choice from 1 to 4: "))
        if choice == 4:
            exit()
        elif choice == 1:
            self.account_details()
        elif choice == 2:
            amount = int(input("Please Enter the amount to be deposited: "))
            self.deposite(amount)
        elif choice == 3:
            amount = int(input("Please Enter the amount to be withdrawn: "))
            self.withdraw(amount)
        else:
            print("Invalid Choice, Bye Bye!!")

acc1 = BankAccount()


        
        
        
        