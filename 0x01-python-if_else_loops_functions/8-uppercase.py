#!/usr/bin/python3
def uppercase(str):
    for x in str:
        x = ord(x)
        if x >= 97 and x <= 122:
            x -= 32
        x = chr(x)
        print("{}".format(x), end='')
    print("")
