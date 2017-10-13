#! /usr/bin/env python2
# -*- coding: utf-8 -*- 
import random


SECRET = random.randint(0,20)


def main():
    while True:
        try:
            guess = int(raw_input("Ugani število med 1 in 20: "))
        except ValueError:
            print "Si vnesel število? Probaj še enkrat."
            continue
        if guess == SECRET:
            print "Pravilno, skrito število je bilo %d" % SECRET
            break
        else:
            print "Blizu. Še vztrjaj!\nČe pa imaš dovolj, pritisni CTR + c"

if __name__ == "__main__":
    main()
