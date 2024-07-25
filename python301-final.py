import inquirer
import sys

class account:
    def __init__(self,balance,account_name):
        print("welcome to the all in one banking system")
        self.balance = balance
        self.account_name = account_name
        self.log_file = f"{self.account_name}-transactions.txt"

        try:
            with open(self.log_file,'w') as file:
                file.write(f"New log transactions for {self.account_name}")
        except:
            print("file already exists")




    def withdraw(self ,amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0

        self.balance = self.balance - amount
        with open(self.log_file,'a') as file:
            file.write(f" \n{amount} withdrawn from the account")
           

    def deposit(self ,amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0

        self.balance = self.balance + amount
        with open(self.log_file,'a') as file:
            file.write(f" \n{amount} deposited into the account")
     


    def check_balance(self):
        print(f"{self.balance}")
        with open(self.log_file,'a') as file:
            file.write(f"\nyour current balance is {self.balance}")
    
    # def exits_app(self):
    #     sys.exit()
while True:
    userName = input("enter the user id of your account: ")
    try:
        currBalance = int(input("enter your current balance: "))
    except:
        print("enter a valid input")
    newAcc = account(currBalance,userName)
    while True:
        choices = ['Deposit', 'Withdrawal', 'Balance check','exit']

      
        questions = [
            inquirer.List('choice',
                        message="Choose a process",
                        choices=choices,
                        ),
        ]

        
        answers = inquirer.prompt(questions)

       
        selected_option = answers['choice']
        if selected_option == 'Deposit':
            try:
                Deposit_balance = int(input("enter the balance you want to deposit: "))
            except:
                print("enter a valid input")         
            newAcc.deposit(Deposit_balance)
        elif selected_option == 'Withdrawal':
            try:
                Withdrawal_balance = int(input("enter the balance you want to Withdrawal: "))
            except:
                print("enter a valid input")         
            newAcc.withdraw(Withdrawal_balance)
        elif selected_option == 'Balance check':
            newAcc.check_balance()
        elif selected_option == 'exit':
            print('exiting your account')
            break
    print("__do you want to exit the app__")
    choices = ['yes','no']

    
    questions = [
        inquirer.List('choice',
                    message="Choose a process",
                    choices=choices,
                    ),
    ]

    
    answers = inquirer.prompt(questions)

    
    selected_option = answers['choice']

    if selected_option == 'yes':
        print("Exiting App")
        break
    else:
        continue






