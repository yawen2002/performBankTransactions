#create log file:
fp=open("MyAccounts.txt",'a')
import datetime
class BankAccount:
    """Help manage different bank accounts at different banks."""
    __Count = 0 #Number of instances
    def __init__(self,AccID,BNAME,ATYPE,B=0): #assign values to be passed
        self.ID = AccID #Account ID: a 6-digit unique identifier
        self.BankName = BNAME #A character string (2-10 characters)
        self.type = ATYPE #A character string; Valid types: chequing, saving, investment, loan, TFSA, RRSP
        self.balance = B #Default initial balance is zero but user can start with an amount.(int)
        self.__pwd = "" #Private attribute.
        self.__LastAccess=datetime.datetime.now() #Private attribute.
        BankAccount.__Count += 1
        f="{} {:6s} {:8s} {:6d} {:7d}" #formatted printing
        eo=f.format(self.__LastAccess,self.ID,"create",0,self.balance)
        print(eo,file=fp)
    def __del__(self):
        BankAccount.__Count -= 1
        print ("Deleting Account instance!")
        f="{} {:6s} {:10s} {:7d} {:7d}" #formatted printing
        e=f.format(self.__LastAccess,self.ID,"delete",0,self.balance)
        print(e,file=fp)
    def __repr__(self):
        """creates and returns the display string"""
        format_str="{:6s} {:10s} {:10s} {:7d} {}" #formatted printing
        d=format_str.format(self.ID,self.BankName,self.type,self.balance,self.__LastAccess) #the order does not matter.
        print(d,file=fp)
    def withdraw(self,amount):
        self.balance -= amount
        fw="{} {:6s} {:10s} {:7d} {:7d}" #formatted printing
        ew=fw.format(self.__LastAccess,self.ID,"withdraw",amount,self.balance)
        print(ew,file=fp)
    def deposit(self,amount):
        self.balance += amount
        fd="{} {:6s} {:10s} {:9d} {:7d}" #formatted printing
        ed=fd.format(self.__LastAccess,self.ID,"deposit",amount,self.balance)
        print(ed,file=fp)
    def transfer (self,other,amount):
        """transfer amount to account other"""
        self.balance -= amount
        other.balance += amount
        ft="{} {:6s} {:10s} {:7d} {:7d}" #formatted printing
        et=ft.format(self.__LastAccess,self.ID,"transfer",amount,self.balance)
        print(et,file=fp)
        ftt="{} {:6s} {:10s} {:7d} {:7d}" #formatted printing
        ett=ftt.format(other.__LastAccess,other.ID,"transfer",amount,other.balance)
        print(ett,file=fp)
    def get_balance(self):
        return(self.balance)
    def get_count(self):
        return(BankAccount.__Count)
    def __eq__(self,other):
        """Two accounts have the same balance"""
        return(self.balance == other.balance)
    def create_password(self):
        password=input(str("Please enter a password:"))
        if password.isalnum() and (8<=len(password)<=15) and password[0].isupper() and not password.isalpha() and password[-1].isdigit() and not password.isupper():
            print("password accepted")
            self.__pwd=password
        else:
            print("password rejected")
    def verify_password(self,p):
        if self.__pwd == p:
            return True
        else:
            return False
#main program code
MyAccounts_dict={} #Dictionary of Accounts
Account_type=["chequing" , "saving" , "investment" , "loan" , "TFSA" , "RRSP"]
#Option 1
choice=0
while choice != 8:
    print("Application Menu: Welcome to the My Money Management App")
    print("1- Create An Account (Enter Account ID, Bank Name, Account Type and Balance)")
    print("2- Withdraw an amount from an account. (Enter Account ID & Amount)")
    print("3- Deposit an amount to an account (Enter Account ID & Amount)")
    print("4- Transfer an amount between accounts (Enter From: and To: Accounts and Amount)")
    print("5- Get balance of a given account (Enter Account ID)")
    print("6- Delete an account (Enter Account ID)")
    print("7- Display the log file.")
    print("8- Exit.")
    choice=int(input("Select an option by entering its number or 8 to exit:"))
    if choice == 1:
        account=input("Enter account info:")
        account=account.split(",")
        if not (account[2]in Account_type):
            print("Account type is not valid.")
        else:
            MyAccounts_dict[account[0]]=BankAccount(account[0],account[1],account[2],int(account[3])) #Account ID is key in dictionary, value is BankAccount object
            print("Your account is created.")
            MyAccounts_dict[account[0]].create_password()
    elif choice == 2:
        n=input("Enter Account ID:")
        if (n in MyAccounts_dict):
            password=input("Enter password:")
            if MyAccounts_dict[n].verify_password(password):
                r=int(input("Enter the amount to withdraw:"))
                if r<MyAccounts_dict[n].get_balance():
                    MyAccounts_dict[n].withdraw(r)
                    print("Withdraw successfully.")
                    print("Your balance is", MyAccounts_dict[n].get_balance())
                else:
                    print("There is not enough money in your account.")
            else:
                print("Password is not correct.")
        else:
            print("The account does not exist.")
    elif choice == 3:
        m=input("Enter Account ID:")
        if (m in MyAccounts_dict):
            password=input("Enter password:")
            if MyAccounts_dict[m].verify_password(password):
                z=int(input("Enter the amount to deposit:"))
                MyAccounts_dict[m].deposit(z)
                print("Deposit successfully.")
                print("Your balance is",MyAccounts_dict[m].get_balance())
            else:
                print("Password is not correct.")
        else:
            print("The account does not exist.")
                
    elif choice == 4:
        a=input("Transfer money from:")
        b=input("Transfer money to:")
        c=int(input("Transfer amount:"))
        if (a in MyAccounts_dict):
            if (b in MyAccounts_dict):
                password=input("Enter password:")
                if MyAccounts_dict[a].verify_password(password):
                    if c<MyAccounts_dict[a].get_balance():
                        MyAccounts_dict[a].transfer(MyAccounts_dict[b],c)
                        print("Transfer successfully.")
                    else:
                        print("There is not enough money.")
                else:
                    print("Password is incorrect.")
            else:
                print("The account which money is going to does not exist.")
        else:
            print("The account which money is going from does not exist.")
    elif choice == 5:
        d=input("Enter Account ID:")
        if (d in MyAccounts_dict):
            password=input("Enter password:")
            if MyAccounts_dict[d].verify_password(password):
                print("The account balance is", MyAccounts_dict[d].get_balance())
            else:
                print("Password is incorrect.")
        else:
            print("The account ID does not exist.")
    elif choice == 6:
        ei=input("Enter Account ID:")
        if ei in MyAccounts_dict:
            password=input("Enter password:")
            if MyAccounts_dict[ei].verify_password(password):
                del MyAccounts_dict[ei]
                print("Delete successfully.")
            else:
                print("Password is incorrect.")
        else:
            print("The Account ID does not exist.")
    elif choice == 7:
        fp.close()
        fp=open("MyAccounts.txt",'r')
        for l in fp:
            print(l)
        fp.close()
        fp=open("MyAccounts.txt",'a')
#Option 8
exit
