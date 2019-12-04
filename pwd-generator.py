#!/usr/bin/env python3
import secrets
import string
import sys

chars = string.ascii_letters + string.digits + "!@#$%&*?"

number = int(sys.argv[1])
passlen = int(sys.argv[2])

def generate_pwd():
    password = "".join(secrets.choice(chars) for i in range(passlen))
    yield password

print(f"Printing {number} password(s) of length {passlen}:")

for i in range(number):
    print(generate_pwd().__next__())
