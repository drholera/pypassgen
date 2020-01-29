# Python Password Generator
# Version 1.1

# import random: needed to build out password and determin lenght if user does not specify one
# import string: needed to create an array of all possible characters from which to build password from
import random, string

# Store all possible characters
characters = string.printable

def build_password(passlen):
    new_pass_list = []
    
    for char in range(0,passlen + 1):
        rand_num = random.randint(0,99)
        char = characters[rand_num]
        new_pass_list.append(char)
    
    new_pass = ''.join([str(elm) for elm in new_pass_list])
    print(new_pass)


# Prompt user for a password lenght, if none is given, randomly assign one from 10-15 characters in lenght
try:
    user_response = int(input('Enter a password lenght (Press Enter for random lenght): '))
except ValueError:
    print('You did not enter a password lenght, so your new password will have a random lenght between 10-15 characters')
    user_response = random.randint(10,20)
    # Call function to build password
    build_password(user_response)

else:
    build_password(user_response)