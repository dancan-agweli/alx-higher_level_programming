#!/usr/bin/python3
import hidden_4
if __name__ == '__main__':
    x = dir(hidden_4)

    for y in range(len(x)):
        if x[y][:2] != '__':
            print(x[y])
