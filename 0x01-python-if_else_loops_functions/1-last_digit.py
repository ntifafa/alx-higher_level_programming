#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# # convert int to str
# output = str(number)
# # slice last digit and assign
# last_digit = int(output[-1])

# ensure negative output carries through to last digit
if number < 0:
    print(f'last digit of {number} is -{(number * -1) % 10} \
and is less than 6 and not 0')

elif number % 10 > 5:
    print(f'last digit of {number} is {number % 10} and is greater than 5')

elif number % 10 == 0:
    print(f'last digit of {number} is {number % 10} and is 0')

elif number % 10 < 6 and number % 10 != 0:
    print(f'last digit of {number} is {number % 10} and is less than 6 \
and not 0')
