#!/usr/bin/python3
for i in range(0, 90):
    for j in range(i+1, 10):
        between = ", "
        if i == 8:
            between = "\n"
        print("{:d}{:d}".format(i, j), end=between)
