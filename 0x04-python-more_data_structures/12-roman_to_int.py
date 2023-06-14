#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    rom_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    output = 0
    prev_val = 0

    for digit in roman_string[::-1]:
        val = rom_d.get(digit, 0)
        if val >= prev_val:
            output += val
        else:
            output -= val
            prev_val = val
    return output
