import random

letters = "qwertyuiopasdfghjklzxcvbnm"
symbols = ",./;'[]\=-~!@#$%^&*()`{}|:\"<>?"
numbers = "1234567890"

master_password = (
    # This will be the password of all passwords
        [input("Enter The Master Password\nUsername: "), 
        input("Enter Password: ")]
    )
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
        username = input("Enter Your Username: ")
        password = None
        
        choice = input("Would You Like a Random Password? (y/n): ")
        
        if choice == "y":
            caps, syms, nums, chars = (
                input("Enter # Caps: "),
                input("# Syms: "),
                input("# Nums: "), 
                input("# Chars: ")
            ) 
            password = random_password(caps, syms, nums, chars)
        else:
            password = input("Enter Your Password: ") 
                       
        saved_logins.append([domain, username, password])
        print("Password Saved")
        
        more = input("Do You Have More Logins?: (y/n)")
        if more.lower() == "y":
            pass
        else:
            break
        
def access_logins():
    num_tries = 0
    while True:
        username = input("Enter Your Master Username: ")
        password = input("Enter Your Master Password: ")
        if master_password == [username, password]:
            site_req = input("Which Site's login Info Do You Want?: ")
            for site in saved_logins:
                if site[0] == site_req:
                    print("Username: " + site[1] + "\nPassword: " + site[2])
                    break #breaks from while loop
            print("Anything Else?")
            choice = input("(Yes/No):")
            if choice == "yes":
                pass
            else:
                break
        else:
            print("Login FAILED! Try Again")
            num_tries += 1  
    
while True:
    choice = input("Do You Want To Add or Access Passwords?: (Add/Access/X)")
    if choice.lower() == "add":
        add_login()
    elif choice.lower() == "access":
        access_logins()
    elif choice.lower() == "x":
        break
    else:
        print("Invalid Choice! Please Enter A Valid Choice!")