#!/usr/bin/python3
for num in range(0, 100):
    between = ", "
    if num == 99:
        between = "\n"
    print("{:02}".format(num), end=between)
