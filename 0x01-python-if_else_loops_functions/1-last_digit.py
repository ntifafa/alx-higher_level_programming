#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# convert int to str
output = str(number)
# slice last digit and assign
last_digit = int(output[-1])
# ensure negative output carries through to last digit
if number < 0:
    last_digit = -last_digit
    print(f'last digit of {number} is {last_digit} and is less than 6 \
and not 0')

elif last_digit > 5:
    print(f'last digit of {number} is {last_digit} and is greater than 5')

elif last_digit == 0:
    print(f'last digit of {number} is {last_digit} and is 0')

elif last_digit < 6 and last_digit != 0:
    print(f'last digit of {number} is {last_digit} and is less than 6 \
and not 0')
