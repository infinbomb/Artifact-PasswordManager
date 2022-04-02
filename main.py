import random

letters = "qwertyuiopasdfghjklzxcvbnm"
symbols = ",./;'[]\=-~!@#$%^&*()`{}|:\"<>?"
numbers = "1234567890"

master_username = input("Enter MasterUsername: ")
master_password = input("Enter MasterPassword: ")
master_password = [master_username, master_password]
    # This will be the password of all passwords

print(master_password)
saved_logins = []
# This will be turned into a 2D array
# To access Enter row(1, 2, 3, ...) and 
# column(0, 1, 2) like so: saved_logins[][]  

def random_password(num_caps, num_sym, num_num, num_char):
    word = ""
    available_values = []
    for char in range(num_char):
        word += (random.choice(letters))
        # word is a lowercase string with random letters
    for x in range(num_char):
        available_values.append(x)
    if num_sym == 0 and num_num == 0 and num_caps == 0:
        pass
    else:                            
        for x in range(num_caps):
        # change for number of uppercase
            choice = random.choice(available_values)
            new_char = word[choice].upper()
            # changes the picked letter to uppercase
            word = word.replace(word[choice], new_char)
            available_values.remove(choice)
        for x in range(num_sym):
            choice = random.choice(available_values)
            new_char = random.choice(symbols)
            # picks a random symbol
            word = word.replace(word[choice], new_char)
            available_values.remove(choice)
        for x in range(num_num):
            choice = random.choice(available_values)
            new_char = random.choice(numbers)
            # picks random number from list
            word = word.replace(word[choice], new_char)
            available_values.remove(choice)
    return word    

def add_login():
    while True:
        domain = input("Enter Site: ")
        done = False
        
        # Checks if another login with same domain already exists
        for site in saved_logins:
            if site[0] == domain:
                print("You Already Have A Login For This Site")
                repeat = input("Do You Want to Add Another? (Y/N)")
                if repeat.lower() == "y":
                    new_username = input("Enter UserName: ")
                    new_password = input("Enter Password: ")
                    saved_logins.append([domain, new_username, new_password])
                    done == True
                    break
                elif repeat.lower() == "n":
                    print("Please Request to Access Login")
                    done = True
                    break 
        if done == True:
            break # Breaks from while loop and from function
                     
        username = input("Enter Your Username: ")
        password = None # Needs to be initated first
        
        choice = (input("Would You Like a Random Password? (y/n): ")).lower()
        
        if choice == "y":
            caps, syms, nums, chars = (
                int(input("Enter # Caps: ")),
                int(input("# Syms: ")),
                int(input("# Nums: ")), 
                int(input("# Chars: "))
            ) 
            if (int(caps) + (int(syms) + int(nums)) <= chars):
                password = random_password(caps, syms, nums, chars)
            else: 
                print("Please Have A Valid Number of Requirements (too many for # of characters)")
                caps, syms, nums, chars = (
                int(input("Enter # Caps: ")),
                int(input("# Syms: ")),
                int(input("# Nums: ")), 
                int(input("# Chars: "))
                ) 
                password = random_password(caps, syms, nums, chars)
            print("Your Password is: " + password)
        elif choice == 'n':
            password = input("Enter Your Password: ") 
        else: 
            print("Please Enter A Valid Choice")
                       
        saved_logins.append([domain, username, password])
        print("Password Saved")
        
        more = input("Do You Have More Logins?: (y/n)")
        if more.lower() == "y":
            pass
        else:
            break
        
def access_logins():
    num_tries = 0 # Weak Security But Good for now

    while True:
        if num_tries < 3:
            username = input("Enter Your Master Username: ")
            password = input("Enter Your Master Password: ")
            if master_password == [username, password]:
                for site in saved_logins:
                    print("Site: " + site[0], sep = ", ")
                    print("User: " + site[1], sep = ", ")
                    print("Pass: " + site[2])
                print("Anything Else?")
                choice = (input("(Yes/No):")).lower()
                if choice == "yes":
                    break #while break
                elif choice == "no":
                    exit()
            else:
                print("Login FAILED! Try Again")
                num_tries += 1  
        else:
            print("Invalid Login! You have been locked out!")
            exit()
    
while True:
    choice = input("Do You Want To Add or Access Passwords?: (Add/Access/X)")
    if choice.lower() == "add":
        add_login()
    elif choice.lower() == "access":
        access_logins()
    elif choice.lower() == "x":
        print("Thanks for using my program!")
        exit()
    else: 
        print("Invalid Choice! Please Enter A Valid Choice!")