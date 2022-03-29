import random

letters = "qwertyuiopasdfghjklzxcvbnm"
symbols = ",./;'[]\=-~!@#$%^&*()`{}|:\"<>?"
numbers = "1234567890"

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
 
test = random_password(1, 1, 1, 12)
print(test)

