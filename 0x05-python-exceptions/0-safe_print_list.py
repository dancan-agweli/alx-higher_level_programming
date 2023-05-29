#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    al = 0
    for y in range(x):
        try:
            print(my_list[y], end='')
            al += 1

        except Exception as error:
            break
    print('')
    return al
