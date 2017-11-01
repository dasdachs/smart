#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""Get the number of us viewers for a given season."""
import argparse
import re

import requests
from bs4 import BeautifulSoup


def get_season(season):
    """Get the correct wiki page for a given season.
    :param season: int, the season
    :return: a string representing the correct wiki page
    """
    if not 1 <= season <= 7:
        print "Please select a sesoon from 1 to 7."
    base_url = "https://en.wikipedia.org/wiki/"
    season_url = "Game_of_Thrones_(season_{})".format(season)
    return base_url + season_url


def get_viewers(url):
    """Get the total number of us viewers.
    :param url: the url to visit, a str
    :return: the number of viwers (million)
    """
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html5lib")
    table = soup.find("table", class_="wikiepisodetable")
    # Omit the header and skip all the descriptions (every second)
    rows = table.find_all("tr")[1::2]
    sub = re.compile(r"\[\d+\]")
    num = 0
    for row in rows:
        # The text includes the quote
        # so we clean it with a regex
        number = re.sub(sub, "", row.find_all("td")[-1].getText())
        num += float(number)
    return num


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get the number of US viewers of a give GoT season."
    )
    parser.add_argument(
        "--season",
        type=int,
        help="What season of GoT are you interesed in. Defaults to 1."
    )
    args = parser.parse_args()
    season = args.season if args.season else 1
    print "Getting the data for season %d." % season
    url = get_season(args.season)
    viewers = get_viewers(url)
    print "The total number of US viewers of GoT S %d is %.2f million." % (season,
                                                                           viewers)
