#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    x = ''
    for w in my_list:
        if w % 2 == 0:
            x.append(True)
        else:
            x.append(False)

    return x
