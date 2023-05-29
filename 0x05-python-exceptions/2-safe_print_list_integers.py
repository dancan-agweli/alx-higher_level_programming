#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0
#print the num
    for k in range(x):
        try:
            if type(my_list[k]) is int and num != x:
                print('{:d}'.format(my_list[k]), end='')
                num += 1
        except TypeError:
            continue

    print()

    return num
