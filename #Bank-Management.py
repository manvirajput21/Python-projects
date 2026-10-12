#Bank management system
class account:
    def __init__(self, name, number , balance):
        self.name = name
        self.number = number
        self.balance = balance
        self.history = []
    def display(self):
         print('ACC HOLDER NAME "{} " ACCOUNT NO "{}" CURRENT BALANCE "{}" '.format(self.name , self.number,self.balance))
    
accounts = []
    
def add():
     name = input("ENTER ACC HOLDER NAME ")
     number = int(input("ENTER ACC NUMBER"))
     balance=float(input("ENTER INITIAL BALANCE"))
     a= account(name,number,balance)
     accounts.append(a)
     print("ACCOUNT CREATED SUCCESFULLY")
        
        
def display():
    if len(accounts)==0:
        print("NO ACCOUNT FOUND")
    else:
        for a in accounts:
            a.display()

def search_account(number):
    for a in accounts:
        if a.number == number:
             return a
    return None

def deposit():
    number = int(input("ENTER ACC NUMBER"))
    a= search_account(number)

    if a: 
        amount = float(input("ENTER AMOUNT TO BE DEPOSIT"))
        if amount > 0:
            a.balance= a.balance + amount
            a.history.append('DEPOSIT "{}" ' .format (amount))
            print("MONEY DEPOSIT SUCCESFULLY")
            print("CURRENT BALANCE:", a.balance)
        else:
            print("NO INV AMT")
    else:
         print("NO ACCOUNT FOUND")
def WITHDRAWN():
    number = int(input("ENTER ACC NUMBER"))
    a= search_account(number)

    if a: 
        amount = float(input("ENTER AMOUNT TO BE WITHDRWN"))
        if amount > 0:
            a.balance= a.balance - amount
            a.history.append('WITHDRAWN "{}" ' .format (amount))
            print("MONEY WITHDRAWN SUCCESFULLY")
            print("CURRENT BALANCE:", a.balance)
        else:
            print("NO INV AMT")
    else:
         print("NO ACCOUNT FOUND")

def Checkbal():
    number = int(input("ENTER ACCOUNT NUMBER: "))
    a = search_account(number)

    if a:
        print("ACCOUNT HOLDER:", a.name)
        print("ACCOUNT NUMBER:", a.number)
        print("NET BALANCE:", a.balance)
    else:
        print("ACCOUNT NOT FOUND")
def Transaction_list():
    number = int(input("ENTER ACCOUNT NUMBER: "))
    a = search_account(number)

    if a:
        print("\n--- TRANSACTION HISTORY ---")
        print("ACCOUNT HOLDER:", a.name)
        print("ACCOUNT NUMBER:", a.number)

        for transaction in a.history:
            print(transaction)
    else:
        print("ACCOUNT NOT FOUND")
def main():
      while True:
        print("\n--- BANK MANAGEMENT SYSTEM ---")
        print("1. ADD ACCOUNT")
        print("2. DISPLAY ALL ACCOUNTS")
        print("3. SEARCH ACCOUNT")
        print("4. DEPOSIT MONEY")
        print("5. WITHDRAW MONEY")
        print("6. CHECK BALANCE")
        print("7. TRANSACTION HISTORY")
        print("8. EXIT")

        choice = input("ENTER YOUR CHOICE: ")

        if choice == '1':
            add()
        elif choice == '2':
            display()

        elif choice == '3':
            number = int(input("ENTER ACCOUNT NUMBER: "))
            a = search_account(number)

            if a:
                a.display()
            else:
                print("ACCOUNT NOT FOUND")
        elif choice == '4':
            deposit()
        elif choice == '5':
            WITHDRAWN()
        elif choice == '6':
            Checkbal()
        elif choice == '7':
            Transaction_list()
        elif choice == '8':
            print("THANK YOU FOR USING OUR BANK")
            break
        else:
            print("INVALID CHOICE")


main()

         
            
            
            
            
            
            
            
                
    
    
    