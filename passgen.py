# Python Password Generator
# Version 1.0

# Import packages
import string, random

# Get a random word from words.txt
def get_word():
    '''
    Purpose: Retrieve a random word from the words.txt file
    Modify: You can add/delete words as needed, must be on a single
    line and seperated by single spaces. 
    '''
    words = open('words.txt', 'r')
    line = words.readline()

    rand_num = random.randint(0,len(line.split()))

    return line.split()[rand_num]

# Build password
def build_pass(pass_len):
    '''
    Purpose: Build a string using a selected word and injecting
    numbers and special characters
    '''
    random_word = get_word()
    rand_num = random.randint(90, 101)
    