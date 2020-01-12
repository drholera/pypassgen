# Python Password Generator
# Version 1.0

# Import packages
import random

# Get a random word from words.txt
def get_word():
    '''
    Purpose: Retrieve a random word from the words.txt file
    Modify: You can add/delete words as needed, must be on a single
    line and seperated by single spaces.
    '''
    # Store words in local variale
    words = open('words.txt', 'r')
    line = words.readline()
    # Seperate words using spaces
    rand_num = random.randint(0,len(line.split())-1)
    # Return a randomly selected word
    return line.split()[rand_num]

# Build password
def build_pass():
    '''
    Purpose: Build a string using a selected word and injecting
    numbers and special characters
    '''
    # 1. Retrieve a random work from the words.txt file
    random_word = get_word()
    # 2. Setup special characters and numbers
    special_chars = [
        '!', '@', '#', '$', '%', '&', '*', '0',
        '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    # 3. Setup empty string as a placeholder for new password
    new_pass = ''
    # 4. Loop through every character in random_word
    for letter in random_word:
        pass_len = len(new_pass)
        special_len = len(special_chars)
        # Create random numbers
        rand_num1 = random.randint(0, special_len)
        rand_num2 = random.randint(0, pass_len)
        # 5. Inject special characters or numbers into the new password
        new_pass += letter
        new_pass += special_chars[rand_num1-1]

        # 6. Capatalize a random letter
        new_pass = new_pass[:rand_num2] \
            + new_pass[rand_num2].upper() \
            + new_pass[rand_num2+1:]
    return new_pass

def write_pass():
    '''
    Purpose: Save the newly created password into a local txt file
    '''
    with open('saved_passwords.txt', 'a') as log:
        log.write(f'Saved password: {build_pass()}\n')

write_pass()