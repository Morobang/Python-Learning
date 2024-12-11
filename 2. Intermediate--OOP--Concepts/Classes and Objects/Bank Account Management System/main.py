"""
Write a program that implements a simple bank account management system. The program should allow users to create bank accounts, deposit and withdraw money, and view account details.
Features to Implement
1. Create a Bank Account
Allow users to create a new bank account with an account holder's name and an optional initial balance.
2. Deposit Funds
Allow users to deposit money into their bank account.
3. Withdraw Funds
Allow users to withdraw money from their bank account, ensuring they do not overdraw.
4. Check Balance
Allow users to view their current account balance.
5. Display Account Information
Provide a method to display the account holder's name and current balance.
"""


class BankAccount:
    #Class Variables used to count the number of accounts in the system
    number_of_bank_accounts = 0


    def __init__(self,account_no,name_of_bank,user_name,balance):
        self.accountNo = account_no
        self.nameOfBank = name_of_bank
        self.userName = user_name
        self.balance = balance
        BankAccount.number_of_bank_accounts +=1

def create_account():
        print("Fill In the information where requried".title())
        bank_account = BankAccount(int(input("enter any account you want: ".title())), str(input("enter any bank name you want: ".title())),int(input("enter your name: ".title())),int(input("enter any balance you want: ".title())))

def action_choice():
    print("1. Create An Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Account")
    choice = int(input("What Would you like to do: ".title()))



print("Wellcome to bank management")
action_choice()
