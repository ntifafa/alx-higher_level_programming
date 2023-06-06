#!/usr/bin/python3
for ascii_code in range(97, 123):
    if ascii_code == 113 or ascii_code == 101:
        ascii_code += 1
        continue
    else:
        print("{}".format(chr(ascii_code)), end="")
