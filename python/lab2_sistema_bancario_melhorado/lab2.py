#!/bin/python

# Desafio 2: melhorando o sistema bancario do desafio 1.


#  ---- FUNCTIONS ---


# Main Menu - chooses between normal user and admin
def show_main_menu():
    print( """
    ************************************
    **            WELCOME!            **
    ************************************
    **	[1] - Administrator           **
    **	[2] - User                    **
    **	[3] - Quit                    **
    **                                **
    ************************************
    """
    )



# Administrator Menu - shows admin's options
def show_admin_menu():
    print( """
    ************************************
    **         MANAGER OPTIONS        **
    ************************************
    **	[1] - Create User             **
    **	[2] - Remove User             **
    **	[3] - Update User             **
    **	[4] - Create Account          **
    **	[5] - Delete Account          **
    **	[6] - Quit                    **
    **                                **
    ************************************
    """
    )



# User Menu - shows options for the normal user
def show_user_menu():
    print( """
    ************************************
    **        CHOOSE AN OPTION        **
    ************************************
    **	[1] - Deposit                 **
    **	[2] - Withdraw                **
    **	[3] - Check Statement         **
    **	[4] - Quit                    **
    **                                **
    ************************************
    """
    )



# Checks if the user ID informed is in the database
def id_checker(**kwargs):
    id_number = input("Enter ID Code: ")
    while id_number not in users.keys():
        id_number = input("User not found!\nTry again: ")
    return id_number



# Validating username and password
def authenticator(id_number, **kwargs):

    username = input("Enter your name: ")
    while username.title() not in users[id_number].values():
        username = input("Name not found!\nTry again: ")

    password = input("Enter your password: ")
    while password not in users[id_number].values():
        password = input("Password not found!\nTry again: ")

    return username, password



# Creating Users
def user_add(*, id_number, name, password, admin, address, birth_date):

    user = { 
        id_number: {
        "name": name,
        "password": password,
        "is_admin": admin,
        "address": address,
        "birth_date": birth_date,
        "is_infractor": False
        }
    }
    return user



# Accounts chooser
def accounts_chooser(id_number, accounts):

    this_user_accs = [i for i in accounts if id_number in i.values()]
    if len(this_user_accs) == 0:
        print("\nYou have no accounts registered in your name. Please, contact the manager.\n\n")
    else:
        print("\nThe following accounts were found: \n")
        accs_ids = []  # let's store the accounts ids                    
        j = 0
        for i in this_user_accs:
            accs_ids.append(i.get("account_id"))
            print(f"Account ID: {accs_ids[j]}")
            j += 1

        print("\nChoose one account [type its number]:  ")
        acc = '-1'
        while int(acc) not in accs_ids:
            acc = input("Accound ID: ")

    return acc



# ---- MAIN ----

login = []            # holds username and password
id_number = ''        # id number or CPF
is_admin = False      # privileges - admin or normal user
address = ""          # format: number, street, city, State, Zip
birth_date = ""       # format: month-day-year
PENALTY = 40.0        # we don't take kindly to morons here
BANK_ID = "0001"      # this can't change
account_id = 1        # auto explanatory
user_id = ''          # user associated with the given account
withdraw_limit = 0.0  # how much per withdraw the user may get
withdraws = 0         # how many withdraws per day

# Accounts form:
accounts = [{"bank_id": BANK_ID, "account_id": 0, "user_id": '??', "account_type": '', "withdraws": 0, "withdraw_limit": 0.0, "balance": 0.0}]

# User form: root and test user provided
users = {
    "0000": {
    "name": "Root",
    "password": "1111",
    "is_admin": True,
    "birth_date": "month-day-year",
    "address": "num, street, city, state, 000000",
    "is_infractor": False
    },

    "9999": {
    "name": "Foo",
    "password": "bar",
    "is_admin": False,
    "birth_date": "month-day-year",
    "address": "num, street, city, state, 000000",
    "is_infractor": False
    }
}

# statement form: each user must have its own operations registered to its id
statement = [{"user_id": '?',"account_id": '', "op_type": 'deposit/withdraw', "value": 1.0, "balance": 1.0}]        


while True:

    show_main_menu()
    option = input("Choose an option: ")


    ## User is Administrator
    if option == '1':

        # Checking whether the user exists or not
        id_number = id_checker(**users)


        # Making sure the user has Administrator privileges
        if users[id_number]["is_admin"] == True:

            # Validating user's name and password
            login = authenticator(id_number, **users)

            while True:

                # Finally showing Administrator's possible actions
                show_admin_menu()
                action = input("Choose an action: ")


                # Adding users
                if action == '1':

                    print("\n--- ADD USER ---\n\n")

                    # Setting the level of privileges for the new user
                    is_admin = True if 'y' in input("Is the user a admin [y, n]? ").lower() else False

                    users.update(user_add(
                        id_number=input("Enter user ID Code: "),
                        name=input("Enter user name: ").title(),
                        password=input("Enter user password: "),
                        admin=is_admin,
                        address=input("Enter user address: "),
                        birth_date=input("Enter user birth date: ")
                        )
                    )
                    print("\n")

                # Deleting Users
                elif action == '2':

                    print("\n--- REMOVE USER ---\n\n")

                    # Checking whether the user exists
                    id_number = id_checker(**users)

                    # Removes the user by its ID
                    if input("Are you sure [y, n]? ").lower() == 'y':
                        print(users.keys())
                        users.pop(id_number)
                        print(users.keys())
                    else:
                        print("Aborted!\n")

                # Update User Info
                elif action == '3':

                    print("\n--- UPDATE USER INFO ---\n\n")

                    id_number = id_checker(**users)
                    print("User status before update: \n", users[id_number])

                    while True:

                        key = input("Enter a key to update: ")
                        value = input("Enter the info: ")

                        users[id_number].update({key: value})
                        print("User status after update: \n", users[id_number])

                        if 'n' in input("Do another change? [y, n]: ").lower():
                            break

                # Creates a bank account for an user
                elif action == '4':

                    account_id +=1
                    print("\n--- CREATE ACCOUNT FOR USER ---\n\nInform the user ID bellow.\n")

                    id_number = id_checker(**users)

                    # What type of bank account it should be?
                    acc_type = input("Choose an account type \n[1] savings \n[2] checking \n[3] student\n\n:: ")
                    while acc_type != '1' and acc_type != '2' and acc_type != '3':
                        acc_type = input("Please, choose a valid type: ")

                    # adding some differences between account types
                    if acc_type == '1':

                        withdraw_limit = 600.0
                        withdraws = 5
                        acc_type = "savings"

                    elif acc_type == '2':

                        withdraw_limit = 1000.0
                        withdraws = 10
                        acc_type = "checking"

                    else:

                        withdraw_limit = 400.0
                        withdraws = 3
                        acc_type = "student"


                    # creating the account
                    accounts.append({
                        "bank_id": BANK_ID,
                        "account_id": account_id,
                        "user_id": id_number,
                        "account_type": acc_type,
                        "withdraws": withdraws,
                        "withdraw_limit": withdraw_limit,
                        "balance": 0.0,
                    })

                    # Now we update user info with this account's id.
                    # We need different names for each account for this user since the account names
                    # are keys for a dictionary. Let's check how many accounts he has in order
                    # generate different names for each new account:

                    acc_name = "account-" # prefix for the account name
                    i = 0                 # the piece to add to the prefix

                    for index in accounts:
                        if id_number in index.values():
                            i+=1
                    acc_name.join(str(i))

                    # registering account to the user
                    users[id_number].update({f"account-{str(i)}_id": account_id})
                    
                    print(f"New Account ID: {account_id}, User: {users[id_number].get('name')}, Type: {acc_type}")


                # Delete a bank account associated with the user
                elif action == '5':

                    print("\n--- REMOVE ACCOUNT ---\n\nInform the user ID.\n")
                    id_number = id_checker(**users)


                    # acc is a filtered accounts[] to show only the ones owned by the current given id_number
                    acc = [index for index in accounts if id_number in index.values()]
                    if len(acc) == 0:
                        print("\nThis user has no accounts.\n")


                    else:
                        print("\nThe following accounts were found: \n", acc, end="\n")
                        acc_id = input("\nEnter the account ID to delete it: ")

                        # This only affects the filtered acc list, to show what is happening
                        x = len(acc)
                        j = 0
                        for i in range(x):
                            if str(acc[i].get("account_id")) == acc_id:
                                j = i
                                break
                        acc.pop(j)
                        print("\nUser accounts after processing: ", acc, end="\n\n")


                        # This is the actual deletion of the account from the accounts list
                        print("\nTotal number of accounts before deletion: ", len(accounts))
                        x = len(accounts)
                        for i in range(x):
                            if str(accounts[i].get("account_id")) == acc_id:
                                j = i
                                break
                        accounts.pop(j)
                        print("Total number of accounts after deletion: ", len(accounts))


                        # It is also needed to remove the account_id from this user's database.
                        print(f"\nUser {users[id_number].get('name')} before account deletion: \n", users[id_number])

                        for key, valor in users[id_number].items():
                            if valor == int(acc_id):
                                users[id_number].pop(key)
                                break

                        print(f"\nUser {users[id_number].get('name')} after account deletion: \n", users[id_number])
                    

                # Quit
                elif action == '6':
                    break


                # Invalid1
                else:
                    print("\nInvalid Action!\n\n")
                    continue

        else:
            users[id_number].update({"is_infractor": True})
            print("\nYou are not Administrator!",
            f"\nThis violation will cost you R$ {PENALTY}.\n\n")
            print(users)



    ## Normal User
    elif option == '2':

        id_number = id_checker(**users)

        # Validating user's name and password
        login = authenticator(id_number, **users)

        while True:
            show_user_menu()
            action = input("Choose an action: ")


            # Deposit
            if action == '1':
                
                print('\n', 30*'#', '\n', 10*' ', 'DEPOSIT\n', 30*'#', "\n\n")

                # User must be able to choose the account to deposit
                acc_to_dep = accounts_chooser(id_number, accounts)

                # Now we take the deposit value and update the chosen account's balance with it, and it must
                # be registered in the statement for this user.                
                print("\nInform the value to deposit.\n")
                dep_value = -1.0
                while not dep_value > 0:
                    dep_value = float(input("[Real number > 0.0]: R$ "))

                # updating the 'balance' for this specific account with the deposit value from input
                for i in accounts:
                    if id_number == i.get("user_id") and int(acc_to_dep) == i.get("account_id"):
                        temp = i.get("balance")
                        temp += dep_value
                        i.update({"balance": temp})
                        this_acc_balance = i.get("balance") # saving to use bellow
                        print("\nAccount Balance Updated: R$", this_acc_balance, end="\n\n")
        

                # now adding the changes to the statement list
                new_entry = {"user_id": id_number, "account_id": acc_to_dep, "op_type": 'deposit', "value": dep_value, "balance": this_acc_balance}
                statement.append(new_entry)



            # Withdraw
            elif action == '2':
                
                print('\n', 30*'#', '\n', 9*' ', 'WITHDRAW\n', 30*'#', "\n")
                
                # user chooses the account
                acc_to_withdraw = accounts_chooser(id_number, accounts)

                # We must take the input and check if the withdraw value is allowed for this account type
                # and if the user hasn't exceeded the maximum number of withdraws allowed.
                print("\nInform the value to withdraw.\n")                

                # Update 'balance' and 'withdraws' for this specific account                                
                for i in accounts:
                    if id_number == i.get("user_id") and int(acc_to_withdraw) == i.get("account_id"):           
                        
                        while True:

                            wtd_value = float(input("R$ "))

                            if not i.get("withdraws") > 0:
                                print("Number of withdraws exceeded.\nTry again tomorrow.\n\n")
                                break
                            elif not wtd_value <= i.get("withdraw_limit"):
                                print("The value has exceeded the maximum.\nTry a smaller value.\n")
                            elif not i.get("balance") >= wtd_value:
                                print("Balance insufficient.\nTry a smaller valuer.\n")                            
                            elif not wtd_value > 0:
                                print("The value must be positive.\n")
                            else:
                                break
                        
                        # send user back to user menu if withdraws are 0
                        if i.get("withdraws") <= 0:
                            break

                        # update balance subtracting withdraw value
                        temp = i.get("balance")
                        temp -= wtd_value
                        i.update({"balance": temp})         
                        this_acc_balance = i.get("balance")
                        print("\nAccount Balance Updated: R$", this_acc_balance, end="\n\n")

                        # we need to reduce the number of withdraws made each time by -1, but there is a problem
                        # it will eventually be 0, so we need a way to turn it back to the default value for this type
                        # of account every day. This is out of the scope for now.                        
                        temp = i.get("withdraws")
                        temp -= 1
                        i.update({"withdraws": temp})
                        print(f'Withdraws left: {i.get("withdraws")}\n')

                # Now let's add this operation to the statement
                new_entry = {"user_id": id_number, "account_id": acc_to_withdraw, "op_type": 'withdraw', "value": wtd_value, "balance": this_acc_balance}
                statement.append(new_entry)              



            # Check Statement
            elif action == '3':

                print('\n', 30*'#', '\n', 9*' ', 'STATEMENT\n', 30*'#', "\n")
                
                # user chooses the account to check
                acc_to_check = accounts_chooser(id_number, accounts)

                info = 45*'=' + '\n' + 12*' ' + 'Operations Done\n' + 45*'=' + '\n'
                dep_num = 0
                wtd_num = 0                
                balance = [0.00]

                for i in statement:

                    if i.get("user_id") == id_number and i.get("account_id") == acc_to_check:
                        if i.get("op_type") == 'deposit':
                            balance.append(i.get("balance"))
                            dep_num += 1
                            info += f'Deposit  n-{dep_num}: R$ {i.get("value"):.2f}  |  Balance: R$ {i.get("balance"):.2f}.\n'
                        elif i.get("op_type") == 'withdraw':
                            balance.append(i.get("balance"))
                            wtd_num += 1
                            info += f'Withdraw n-{wtd_num}: R$ {i.get("value"):.2f}  |  Balance: R$ {i.get("balance"):.2f}.\n'

                last_balance = balance[len(balance)-1]
                info += 45*'-' + '\n' + f'Balance: R$ {0.00 if len(balance) == 1 else last_balance:.2f}\n' + 45*"=" + '\n\n'
                print(info)

            # Quit
            elif action == '4':
                break

            # Invalid Operation
            else:
                print("\nInvalid Operation!\n")
                continue



    ## Exit Program
    elif option == '3':
        print("\nBYE!\n\n")
        break

    ## Invalid Option
    else:
        print("\nError. This option does not exist!\n\n")
        continue




