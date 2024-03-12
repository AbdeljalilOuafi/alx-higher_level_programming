#!/usr/bin/python3
for alp in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(
        alp if (ord('z') - alp) % 2 == 0 else alp - 32), end='')
