file = open("logins", "a")
# opens a file in append mode that

print("Welcome To Password Manager")

while True:
    choice = input("Logins?: (y/n)")
    if choice == "y":
        website = input("Enter Website: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        
        file.write(website + "\n____________\nUser: " + username + "\nPass: " + password + "\n")
    else:
        break

while True:
    choice = input("Do You Want To Access Passwords?: (y/n)")
    file = open("logins", "r")
    if choice == "y":
        for line in file:
            print(line, end="")
        break
    else:
        break

def delete_passwords():
    file.truncate()
    # clears the file
    
file.close()