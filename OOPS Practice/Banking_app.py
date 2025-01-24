#SOLUTION 3
import time
import os
import json
from tabulate import tabulate
class BankAccount:
    starting_acc_num = 1000 #class attribute
    accounts_file = r"D:\Web Development\Tutorial Practice Codes\Python_Practice\OOPS Practice\accounts.json"
    
    #Constructor
    def __init__(self,acc_num,acc_holder=None,bal=500):
        self.account_number = acc_num
        self.account_holder = acc_holder
        self.balance = bal
        print(f"Account created successfully for {self.account_holder} with minimum balance 500!")
    
    #Deposite function
    def deposite(self,amount):
        if amount <= 0:
            print("Entered Amount must be positive!!")
        else:
            self.balance = self.balance + amount
            print(f"Deposited {amount}. Current balance is {self.balance}.")
    
    #Withdraw Function
    def withdraw(self,amount):
        if amount <= 0:
            print("Withdrawal Amount must be positive!!")
        elif self.balance - amount < 0:
            print("Insufficient balance!")
        else:
            self.balance = self.balance - amount
            print(f"Withdrew {amount}. Current balance is {self.balance}.")
    
    #Function to print account details
    def account_details(self):
        time.sleep(0.5)
        print("\n--- Account Details ---")
        time.sleep(0.2)
        print(f"Account Number: {self.account_number}")
        time.sleep(0.2)
        print(f"Account Holder: {self.account_holder}")
        time.sleep(0.2)
        print(f"Balance: {self.balance}")
        time.sleep(0.2)
        print("-----------------------")
        time.sleep(0.2)
    
    @staticmethod
    def load_accounts():
        try:
            if os.path.exists(BankAccount.accounts_file):
                with open(BankAccount.accounts_file,"r") as file:
                    data = json.load(file)
                    return data["accounts"], data.get("last_account_number",1000)
            return [],1000
        except Exception as msg:
            print("Error:",msg)
    
    @staticmethod
    def save_accounts(accounts,last_account_number):
        try:
            with open(BankAccount.accounts_file,"w") as file:
                data = {
                    "accounts" : accounts,
                    "last_account_number" : last_account_number
                }
                json.dump(data,file,indent=4)
        except Exception as msg:
            print("Error:",msg)
    
    @staticmethod
    def delete_account(accounts,acc_num):
        for account in accounts:
            if account["account_number"] == acc_num:
                confirmation = input("Do you really want to delete account? YES or NO -> ").strip().lower()
                if confirmation == "yes":
                    accounts.remove(account)
                    print(f"Account {acc_num} deleted successfully.")
                    return True
                else:
                    print(f"Account {acc_num} deletion aborted.")
                    return False
        print(f"Account {acc_num} not found.")
        return False
        
#Main program
accounts, last_account_number = BankAccount.load_accounts()

# Progress indicator
def show_progress(message, delay=0.5, dots=3):
    print(message, end="", flush=True)
    for _ in range(dots):
        time.sleep(delay)
        print(".", end="", flush=True)
    print()

# Display accounts in table format
def display_all_accounts(accounts):
    if not accounts:
        print("No accounts found.")
        return

    # Prepare data for tabulation
    table = [
        [acc["account_number"], acc["account_holder"], acc["balance"]]
        for acc in accounts
    ]
    headers = ["Account Number", "Account Holder", "Balance"]

    # Display the table
    print("\n--- All Accounts ---")
    print(tabulate(table, headers=headers, tablefmt="grid"))


while True:
    time.sleep(0.2)
    print("****************************************************")
    print("           Welcome to United Bank")
    print("*****************************************************")
    print("Please choose from below")
    time.sleep(0.1)
    print("1. Create Account")
    time.sleep(0.1)
    print("2. Print account details")
    time.sleep(0.1)
    print("3. Deposit Money")
    time.sleep(0.1)
    print("4. Withdraw Money")
    time.sleep(0.1)
    print("5. Delete account")
    time.sleep(0.1)
    print("6. Print all account details")
    time.sleep(0.1)
    print("7. Exit")
    try:
        choice = int(input("Please Enter the choice from 1 to 7: "))
        if choice >=1 and choice <=7:
            pass
        else:
            print("Invalid input! Please enter a number between 1 and 7.")
            continue    
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 7.")
        continue
    
    #Creating Account logic
    if choice == 1:
        acc_holder = input("Enter account holder name: ")
        new_account = BankAccount(last_account_number,acc_holder)
        last_account_number += 1
        accounts.append({
            "account_number" : new_account.account_number,
            "account_holder" : new_account.account_holder,
            "balance" : new_account.balance
        })
        #accessing a static method with class name
        BankAccount.save_accounts(accounts,last_account_number)
        print("Account created successfully!")
    
    #account details logic
    elif choice == 2:
        try:
            acc_number = int(input("please Enter your account number: "))
        except ValueError as message:
            print("Please enter a valid account number:",message)
            continue
        
        account_found = False  # Flag to track if the account exists
        
        for account in accounts:
            if account["account_number"] == acc_number:
                account_found = True
                time.sleep(0.1)
                print("Account Number->",account["account_number"])
                time.sleep(0.1)
                print("Account Holder Name->",account["account_holder"])
                time.sleep(0.1)
                print("balance->",account["balance"])
                break
        if not account_found:
            print("Account doesn't exists, would you like to create one? If yes, the please press 1")
        
        
    
    #depositing logic
    elif choice == 3:
        try:
            acc_number = int(input("please Enter your account number: "))
        except ValueError as message:
            print("Please enter a valid account number:",message)
            continue
        
        account_found = False  # Flag to track if the account exists
        
        for account in accounts:
            if account["account_number"] == acc_number:
                account_found = True
                try:
                    amount = int(input("Please enter the amount to deposit: "))
                    if amount <= 0:
                        print("Amount must be positive!")
                        continue
                except ValueError as message:
                    print("Please enter a valid amount:",message)
                    continue
                account["balance"] += amount
                print(f"{amount} successfully depositied, current balance is {account["balance"]}")
                break
        if not account_found:
            print("Account doesn't exists")
        
        BankAccount.save_accounts(accounts,last_account_number)
    
    #withdrawing logic
    elif choice == 4:
        try:
            acc_number = int(input("please Enter your account number: "))
        except ValueError as message:
            print("Please enter a valid account number:",message)
            continue
        
        account_found = False  # Flag to track if the account exists
        
        for account in accounts:
            if account["account_number"] == acc_number:
                account_found = True
                try:
                    amount = int(input("Please enter the amount to withdraw: "))
                except ValueError as message:
                    print("Please enter a valid amount:",message)
                    continue
                if account["balance"] <= 0:
                    print("insufficient funds")
                elif account["balance"] - amount < 0:
                    print("insufficient funds")
                else:
                    account["balance"] -= amount
                print(f"{amount} successfully withdrawn, current balance is {account["balance"]}")
                break
            
        if not account_found:
            print("Account doesn't exists")
            
        BankAccount.save_accounts(accounts,last_account_number)
    
    #deleting logic
    elif choice == 5:
        try:
            acc_num = int(input("Enter the account number to delete: "))
            if BankAccount.delete_account(accounts, acc_num):
                BankAccount.save_accounts(accounts, last_account_number)
        except ValueError:
            print("Invalid account number!")
    
    #All accounts logic
    elif choice == 6:
        show_progress("Fetching account details")
        display_all_accounts(accounts)
    
    #exit logic
    elif choice == 7:
        print("Thank you for using United Bank. Goodbye!")
        break
        
            
            
                
                
                    
        

