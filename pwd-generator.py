#!/usr/bin/env python3
from secrets import choice # most secure module for generating random passwords
from string import ascii_letters, digits # imports all letters A-Z lowercase and uppercase, and all 10 digits
from sys import argv # allows use of command-line arguments

characters = ascii_letters + digits + "!@#$%&*?" # initializing our selection of characters

number = int(argv[1]) # number of passwords to be printed
pass_length = int(argv[2]) # length of each password

def generate_pwd():
    password = "".join(choice(characters) for i in range(pass_length))
    yield password

print(f"Printing {number} password(s) of length {pass_length}:")

# displays all passwords
for i in range(number):
    print(generate_pwd().__next__())
