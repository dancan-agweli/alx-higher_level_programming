#!/usr/bin/python3
import sys
if __name__ == "__main__":
    x = len(sys.argv)
    sum = 0

    for y in range(1, x):
        sum += int(sys.argv[y])
    print(sum)
