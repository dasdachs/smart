#! /usr/bin/env python2
# -*- coding: utf-8 -*- 
"""A protoype program for generating lotery numbers."""
import os
import random


def generate_numbers(length):
    """Returns a sorted list of randon numbers.

    :param length: an int, the length of the array
    :return: a list
    """
    # We set a good random seed with the byte size of 1024
    random.seed(os.urandom(1024))
    numbers = []
    while len(numbers) < length:
        number = random.randint(1,39)
        if number not in numbers:
            numbers.append(number)
    return sorted(numbers)

if __name__ == "__main__":
    print "Welcome to the Lottery numbers generator."
    while True:
        l = raw_input("Please enter how many random numbers would you like to have: ")
        try:
            l = int(l)
            break
        except:
            print "Please enter an integer."
    print " ".join([str(x) for x in generate_numbers(l)])
    print "END"


