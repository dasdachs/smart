#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""A cli application to store your contacts."""
import argparse
import os

from src.contact_book import Contact, ContactBook
from src.draw_table import draw_table


# Get the clear screen comand to simulate a minimal UI
CLEAR_SCREEN = "cls" if os.name == "nt" else "clear"


def main(from_file=None):
    """The main method, which is basically a long while loop.

    :param from_file: a path to the file to get the data from
    """
    if from_file:
        # TODO: simple txt, csv or json loading
        pass
    book = ContactBook()
    headers = ["Ime", "Priimek", "Telefonska", "Leto rojstva", "E-pošta"]
    # Start the programm
    print "Wellcome to the Contact Book."
    print "Let's get busy."
    while True:
        os.popen(CLEAR_SCREEN)
        print "SmartNinja Contact book"
        print ""
        print draw_table(book.get_data(), headers)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A cli Contact book.")
    parser.add_argument("--from", type=str,
                        help="Import contacts from a file.")
    args = parser.parse_args()
    main()
