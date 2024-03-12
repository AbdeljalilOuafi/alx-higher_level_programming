#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    last_digit = number % 10
elif number < 0:
    num = -number % 10
    last_digit = num * (-1)

if last_digit > 5:
    phrase = f"and is greater than 5"
elif last_digit < 6 and last_digit != 0:
    phrase = f"and is less than 6 and not 0"
elif last_digit == 0:
    phrase = f"and is 0"

print(f"Last digit of {number} is {last_digit} {phrase}")
