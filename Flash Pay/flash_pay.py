#import needed modules
import os
import sqlite3
import random

#connect to sqlite to get current data and time
with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    query = "SELECT datetime('now', 'localtime');"
    time = cursor.execute(query).fetchone()[0]

#declear global variables
current_year = time[:4]
current_month = time[6]
current_day = time[-1]
otp = ''
balance = 1000.00

users = {}

'''
class Bank:
    pass

class User:
    def __init__(self, name, mid_name, surname, phone):
        self.name = input("Please tell us your first name: ")
        self.mid_name = imput("Please tell us middle name
'''

print("--zzz-zzz-zzz-zzz-zzz-----Welcome to Flash Bank-----zzz-zzz-zzz-zzz-zzz--")
print("Sign Up now to claim your #1000 REWARD!!!")

#get user details as input
print("1.Sign-Up\t\t2.Sign-In")
logs = input('A new User? Press 1 to Sign-Up || Already have an account? Press 2 to Sign-In: ')
if logs == '1':
    print("Please be sure to fill in details correctly as any error will exit the program")
    print("Now Let's Get to know you")
    first_name = input("Enter your First Name: ")
    middle_name = input("Enter your Middle Name: ")
    last_name = input("Enter your Last Name: ")
    phone_number = input("Enter your 11 digits Phone Number: ")

    #create user slot as a file directory
    main_path = "C:/Users/Timothy/Documents/CODES/Flash_Bank/Flash Pay"
    os.mkdir(os.path.join(main_path, f"{phone_number} {first_name} {middle_name} {last_name}"))

    #check if phone number is valid 
    if (len(phone_number) < 11) or (len(phone_number) > 11):
        print("Progress Terminated")
        exit()
    else:
        #update user's information in the file slot as a .txt and .dat files
        detail_file = open(f"C:/Users/Timothy/Documents/CODES/Flash_Bank/Flash Pay/{phone_number} {first_name} {middle_name} {last_name}/{phone_number}.dat", "w")
        detail_file.writelines(f"Name: {first_name} {middle_name} {last_name}\nPhone: {phone_number}")
        detail_file.close()
        detail_file_sec = open(f"C:/Users/Timothy/Documents/CODES/Flash_Bank/Flash Pay/{phone_number} {first_name} {middle_name} {last_name}/{phone_number}.txt", "w")
        detail_file_sec.writelines([f"{first_name}",f"\n{phone_number}"])
        detail_file_sec.close()
    
    print("Noted now let's see what kind of account will suite you")
    day_of_birth = int(input("What date where you born?: "))
    month_of_birth = int(input("What month?: "))
    year_of_birth = int(input("What year? if you don't mind: "))
    day, month, year = day_of_birth, month_of_birth, year_of_birth

    #check age eligibility
    eligibility = int(current_year) - year
    detail_file = open(f"C:/Users/Timothy/Documents/CODES/Flash_Bank/Flash Pay/{phone_number} {first_name} {middle_name} {last_name}/{phone_number}.dat", "a")
    detail_file.writelines(f"\nAge: {eligibility}")
    detail_file.close()
    detail_file_sec = open(f"C:/Users/Timothy/Documents/CODES/Flash_Bank/Flash Pay/{phone_number} {first_name} {middle_name} {last_name}/{phone_number}.txt", "a")
    detail_file_sec.writelines(f"\n{eligibility}")
    detail_file_sec.close()
    if eligibility >= 25:
        account_type = input("What kind of account do you want to create: 1.Current \t2.Savings? ")
        if account_type == '1':
            print("Current Account Created")
            detail_file = open(f"C:/Users/Timothy/Documents/CODES/Flash_Bank/Flash Pay/{phone_number} {first_name} {middle_name} {last_name}/{phone_number}.txt", "a")
            detail_file.writelines("\nAccount type: Current Account")
            detail_file.close()
        elif account_type == '2':
            print("Savings Account Created")
            detail_file = open(f"C:/Users/Timothy/Documents/CODES/Flash_Bank/Flash Pay/{phone_number} {first_name} {middle_name} {last_name}/{phone_number}.txt", "a")
            detail_file.writelines("\nAccount type: Savings Account")
            detail_file.close()
        else:
            print('Invalid Input Progress Terminated')
            exit()
    elif (eligibility >= 18) and (eligibility <= 24):
        print("Student account created automatically a savings account")
        detail_file = open(f"C:/Users/Timothy/Documents/CODES/Flash_Bank/Flash Pay/{phone_number} {first_name} {middle_name} {last_name}/{phone_number}.txt", "a")
        detail_file.writelines("\nAccount type: Savings Account")
        detail_file.close()
    else:
        print("Piggy Bank Account created, A savings account with parental controls activated")
        detail_file = open(f"C:/Users/Timothy/Documents/CODES/Flash_Bank/Flash Pay/{phone_number} {first_name} {middle_name} {last_name}/{phone_number}.txt", "a")
        detail_file.writelines("\nAccount type: Savings Account")
        detail_file.close()

    print("Now let's Secure your account")
    for i in range(4):
        otp += str(random.randint(1,10))
    print(f"Here is your {len(otp)} digit otp code don't share with anyone {otp}")
    re_otp = input("Enter your otp code for confirmation: ")
    if otp == re_otp:
        password = input("Enter a password. NB. must be 8 characters long: ")
        re_password =  input("Retype your password: ")
        if len(password) >= 8 and password == re_password:
            detail_file = open(f"C:/Users/Timothy/Documents/CODES/Flash_Bank/Flash Pay/{phone_number} {first_name} {middle_name} {last_name}/{phone_number}.dat", "a")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
            detail_file.writelines(f"\nPassword: {password}\nBalance: #{balance}")
            detail_file.close()
            detail_file_sec = open(f"C:/Users/Timothy/Documents/CODES/Flash_Bank/Flash Pay/{phone_number} {first_name} {middle_name} {last_name}/{phone_number}.txt", "a")
            detail_file_sec.writelines([f"\n{password}",f"\n{phone_number[1:]}."])
            detail_file_sec.close()
        else:
            exit()
    else:
        exit()
        
    print(f"Account created,\nYour account number is {phone_number[1:]} and account balance is {balance}\nNow restart the program and Sign-In")
elif logs == '2':
    user_slots = []
    path = "C:/Users/Timothy/Documents/CODES/Flash_Bank/Flash Pay"
    files_and_folders = os.listdir(path)
    for folder_name in files_and_folders:
        full_path = os.path.join(path, folder_name)
        if os.path.isdir(full_path):
            user_slots.append(full_path[54:])

            
    details = []
    details_sec = []

    #get users login details
    account_number = input("Enter your account number: ")
    pass_word = input("Enter your password: ")

    #heck if user exists
    for i in user_slots:
        path = "C:/Users/Timothy/Documents/CODES/Flash_Bank/Flash Pay"
        if i[:11] == f"0{account_number}":
            log_file = open(f"{path}/{i}/0{account_number}.txt", "r")
            if log_file != "":
                for line in log_file.readlines():
                    details.append(line)
                log_file.close()

                #check if user account number and password is correct
                if (details[1] == f"0{account_number}\n") and (details[4] == f"{pass_word}\n"):
                    log_file_sec = open(f"{path}/{i}/0{account_number}.dat", "r")
                    for line in log_file_sec.readlines():
                        details_sec.append(line)
                    log_file_sec.close()
                    
                    name = details_sec[0]
                    print(f"Welcome {name[6:]}", end="")
                    print("This is your flash-pay dashboard")
                    carry_on = "n"

                    #loop to keep banking process active
                    while carry_on == "n" and carry_on.upper() == "N":
                        choice = input("What would you like to do: \n1. Withdraw \t 2. Transfer \t3. Check account balance \n4. Fund account \t5. Change password\nChoose an option: ")

                        #withdraw functionality
                        if choice == '1':
                            amount = input("How much would you like to withdraw: #")
                            bal = details_sec[4]

                            #check if amount to withdraw is higher than balance
                            if float(amount) <= float(bal[10:]):
                                print("Please wait why your transaction is in progress...")
                                avail = float(bal[10:]) - float(amount)
                                details_sec[4] = f"Balance: #{avail}"
                                update_file = open(f"{path}/{i}/0{account_number}.dat","w")
                                update_file.writelines(f"{details_sec[0]}{details_sec[1]}{details_sec[2]}{details_sec[3]}{details_sec[4]}")
                                update_file.close()
            
                                print("-zzz-zzz-zzz-----Flash-Pay Reciept-----zzz-zzz-zzz-")
                                print(f"Date/Time:\t{time}")
                                print(f"Name:\t\t{name[6:]}", end="")
                                print(f"Amount:\t\t#{amount}.00")
                                print("---------------------------------------------------")
                                print("\t\tTRANSACTION APPROVED")
                            else:
                                print("Please wait why your transaction is in progress...")
                                print("-zzz-zzz-zzz-----Flash-Pay MMS-----zzz-zzz-zzz-")
                                print(f"Date/Time:\t{time}")
                                print(f"Name:\t\t{name[6:]}", end="")
                                print(f"Amount:\t\t#{amount}.00")
                                print("---------------------------------------------------")
                                print("\t\tINSUFFICIENT FUNDS")

                        #transfer functionality        
                        elif choice == '2':
                            recipient_info = []
                            recipient = input("Enter the recipient account number: ")
                            for i in user_slots:
                                if i[:11] == f"0{recipient}":
                                    #read recipiets info
                                    recipient_sec = open(f"{path}/{i}/0{recipient}.dat", "r")
                                    for line in recipient_sec.readlines():
                                        recipient_info.append(line)
                                        recipient_sec.close()

                                    rec_name = recipient_info[0]
                                    print(f"Account found : {i[12:]}")
                                    amount = input("Enter the amount you would like to transfer: #")
                                    bal = details_sec[4]
                                    rec_bal = recipient_info[4]
                                    if float(amount) <= float(bal[10:]):
                                        print("Please wait why your transaction is in progress...")
                                        avail = float(bal[10:]) - float(amount)
                                        details_sec[4] = f"Balance: #{avail}"
                                        recipient_info[4] = f"Balance: #{float(rec_bal[10:]) + float(amount)}"
                                        
                                        #update user file
                                        update_file_usr = open(f"{path}/{i}/0{account_number}.dat","w")
                                        update_file_usr.writelines(f"{details_sec[0]}{details_sec[1]}{details_sec[2]}{details_sec[3]}{details_sec[4]}")
                                        update_file_usr.close()
                                        
                                        #update recipient file
                                        update_file_rec = open(f"{path}/{i}/0{recipient}.dat", "w")
                                        update_file_rec.writelines(f"{recipient_info[0]}{recipient_info[1]}{recipient_info[2]}{recipient_info[3]}{recipient_info[4]}")
                                        update_file_rec.close()
                                        
                                        print("-zzz-zzz-zzz-----Flash-Pay Reciept-----zzz-zzz-zzz-")
                                        print(f"Date/Time:\t{time}")
                                        print(f"Name:\t\t{name[6:]}", end="")
                                        print(f"Recipient's Name: {rec_name[6:]}", end="")
                                        print(f"Amount:\t\t#{amount}.00")
                                        print("---------------------------------------------------")
                                        print("\t\tTRANSACTION APPROVED")
                                    else:
                                        print("Please wait why your transaction is in progress...")
                                        print("-zzz-zzz-zzz-----Flash-Pay MMS-----zzz-zzz-zzz-")
                                        print(f"Date/Time:\t{time}")
                                        print(f"Name:\t\t{name[6:]}", end="")
                                        print(f"Amount:\t\t#{amount}.00")
                                        print("---------------------------------------------------")
                                        print("\t\tINSUFFICIENT FUNDS")
                                else:
                                    print("Username not found")
                                    
                        #account_balance functionality       
                        elif choice == '3':
                            bal = details_sec[4]
                            print("Please wait why your transaction is in progress...")
                            print("-zzz-zzz-zzz-----Flash-Pay BALANCE-----zzz-zzz-zzz-")
                            print(f"Date/Time:\t{time}")
                            print(f"Name:\t\t{name[6:]}", end="")
                            print(f"Account Bal:\t{bal[9:]}0")
                            print("---------------------------------------------------")
                            
                        #account funding functionality
                        elif choice == '4':
                            print("For flash pay agent use only")
                            #add_on("How much would you like to fund your account with: #")
                            pass

                        #password change functionality
                        elif choice == '5':
                            print("coming soon")
                            pass

                        else:
                            print('Invalid Input')
                            exit()

                        carry_on = input("Would you like to log out[Y/N]: ")
                    

                else:
                    print("Account not found or invalid password")
                    exit()

  
    
            else:
                print("Account not found")
                exit()
else:
    print("Invalid input")
    exit()
