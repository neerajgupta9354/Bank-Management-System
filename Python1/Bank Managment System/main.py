# sourcery skip: collection-into-set, merge-duplicate-blocks, remove-empty-nested-block, remove-pass-body, remove-pass-elif, remove-redundant-if, split-or-ifs, switch
from register import *
from bank import *

status = False
print("Welcome to Our Bank!!!")
while True:
    try:
        register = int(input("Choose any option : " \
        "1. SignUp " \
        "2. SignIn \n" \
        "Enter 1 or 2 for selecting option : "))
        if register in [1, 2]:
                if register == 1 :
                     SingUp()
                if register == 2 :
                     user = SignIn()
                     status = True
                     break
        else:
            print("Invalid Input please choose 1 or 2 options only")
            
    except ValueError:
        print("Invalid Input please choose 1 or 2 options only")


acc_no = exe(f"SELECT acc_no FROM customer WHERE username = '{user}';")


while status:
    try:
        Facilities = int(input("Choose any option : \n" \
        "1. Bank Enquiry \n" \
        "2. Amount Deposit \n" \
        "3. Amount Withdraw\n" \
        "4. Fund Transfer\n" \
        "Enter 1 or 2 for selecting option : "))
        if Facilities in [1, 2 ,3,4]:
                if Facilities == 1 :
                     bobj = Bank(user , acc_no[0][0])
                     bobj.bankenquiry()
                elif Facilities == 2 :
                     while True:
                        try:
                            amount = int(input("Enter amount : "))
                            bobj = Bank(user , acc_no[0][0])
                            bobj.deposit(amount)
                            break
                        except ValueError:
                            print("Enter valid amount")
                   
                elif Facilities == 3 :
                  
                      while True:
                        try:
                            amount = int(input("Enter amount : "))
                            bobj = Bank(user , acc_no[0][0])
                            bobj.withdraw(amount)
                            break
                        except ValueError:
                            print("Enter valid amount")

                elif Facilities == 4 :
                    while True:
                        try:
                            receiver = input("Enter account number : ")
                            amount = int(input("Enter amount : "))
                            bobj = Bank(user , acc_no[0][0])
                            bobj.fundtransfer(receiver , amount)
                            break
                        except ValueError:
                            print("Enter valid amount")
                             
        else:
            print("Invalid Input please choose 1 or 2 options only")
            
    except ValueError:
        print("Invalid Input please choose 1 or 2 options only")