#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""Gets the first 5 quotes from
http://quotes.yourdictionary.com/theme/marriage/
"""
import argparse

import requests
from bs4 import BeautifulSoup


def get_quotes(url, number_of_quotes=5):
    """Gets http://quotes.yourdictionary.com/theme/marriage/
    :param url: the starting page
    :param number_of_quotes: int, the number of quotes to return
    :return: a list of quotes
    """
    response_body = requests.get(url)
    soup = BeautifulSoup(response_body.text, "html5lib")
    tags = soup.find_all("p", class_="quoteContent")
    quotes = []
    number = number_of_quotes if number_of_quotes <= len(tags) else len(tags)
    for tag in range(number):
        quotes.append(tags[tag].getText())
    return quotes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Get the top n quotes on mariage.'
    )
    parser.add_argument(
        "--quotes",
        type=int,
        help="How many quotes do you want."
    )
    args = parser.parse_args()
    num = args.quotes if args.quotes else 5
    print "Getting the quotes ..."
    quotes = get_quotes(
        "http://quotes.yourdictionary.com/theme/marriage/",
        num
    )
    print "Any minute now..."
    print ""
    for quote in quotes:
        print quote + "\n"
