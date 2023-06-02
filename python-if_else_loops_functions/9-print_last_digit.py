#!/usr/bin/env python3
def print_last_digit(number):
    lastD = abs(number) % 10
    print("{:d}".format(lastD), end='')
    return lastD
