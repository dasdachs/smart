#! /usr/bin/env python2
# -*- coding: utf-8 -*- 
"""Simple fizzbuzz script with user input."""
from __future__ import print_function


def fizz_buzz(last_number):
    """Print number from 1 to last_number with fizzbuzz."""
    assert 0 <= last_number <= 100, "Use a number beetwen 1 and 100."
    for num in range(1, last_number+1):
        if num % 15 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)

def get_input():
    """Gets the users input and makes sure that it is a integer."""
    print("This is a simple fizzbuzz program that prints numbers from 1 ton.")
    while True:
        user_input = raw_input("Please enter a number beetwen 1 and 100: ")
        try:
            user_input = int(user_input)
            if not 0 < user_input <=100:
                print("The number should be beetwen 1 and 100.")
                continue
            return user_input
        except:
            print("Please enter a number or press CTRL+c to exit the program.")


if __name__ == "__main__":
    fizz_buzz(get_input())
