#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    alx = len(sys.argv) - 2+1
    if alx == 0:
        print("0 arguments.")
    elif alx == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(alx))
    for x in range(alx):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
