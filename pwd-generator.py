#!/usr/bin/env python3
import string
import random
import sys

chars = string.ascii_letters + string.digits + "!@#$%&*?"

number = int(sys.argv[1])
passlen = int(sys.argv[2])

def generate():
    pwd = "".join(random.sample(chars, passlen))
    yield pwd

for i in range(number):
    print(generate().__next__())