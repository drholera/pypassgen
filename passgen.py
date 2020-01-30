# Python Password Generator
# Version 1.1

# import random: needed to build out password and determin lenght if user does not specify one
# import string: needed to create an array of all possible characters from which to build password from
import random, string
from datetime import datetime

# Get current date information
today = datetime.now()

# Store all possible characters
characters = string.printable

def build_password(passlen):
    '''
    Build new password using randomly selected characters
    '''
    # Iniialize empty list
    new_pass_list = []

    # Format current date
    curr_date = today.strftime("%d/%m/%Y %H:%M:%S")
    
    # Populate list with random characters
    while len(new_pass_list) <= passlen:
        rand_num = random.randint(0,99)
        rand_char = characters[rand_num]
        new_pass_list.append(rand_char)
    
    # Convert list to a single string
    new_pass = ''.join([str(elm) for elm in new_pass_list])

    # Save password into local text file, creates file is it doesn't already exist
    with open('saved_passwords.txt', 'a') as log:
        log.write(f'Password created on {curr_date} : {new_pass}\n')

    # Return completed password
    return new_pass


# Prompt user for a password lenght, if none is given, randomly assign one from 10-15 characters in lenght
try:
    user_response = int(input('Enter a password lenght (Press Enter for random lenght): '))
except ValueError:
    print('Your new password was assigned a random lenght between 10-20 characters')
    user_response = random.randint(10,20)
    # Call function to build password
    print("\nPassword succesfully generated!\n")
    print(build_password(user_response))
    


else:
    print("\nPassword succesfully generated!\n")
    print(build_password(user_response))
    