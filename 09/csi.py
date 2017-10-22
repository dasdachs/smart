#! /usr/bin/env python2
# -*- coding: utf-8 -*- 
"""This is a solution to
https://github.com/smartninja/python-exercises/tree/master/challenges/CSI
"""
DNA = open("dna.txt").read()
GENES = { 
    "Hair color": {
        "Black": "CCAGCAATCGC",
        "Brown": "GCCAGTGCCG",
        "Blonde": "TTAGCTATCGC"
    },
    "Face shape": {
        "Square": "GCCACGG",
        "Round": "ACCACAA",
        "Oval": "AGGCCTCA"
    },
    "Eye color": {
        "Blue": "TTGTGGTGGC",
        "Green": "GGGAGGTGGC",
        "Brown": "AAGTAGTGAC"
    },
    "Gender": {
        "Female": "TGAAGGACCTTC",
        "Male": "TGCAGGAACTTC"
    },
    "Race": {
        "White": "AAAACCTCA",
        "Black": "CGACTACAG",
        "Asian": "CGCGGGCCG"
}}

SUSPECTS = [
    {
        "name": "Eva",
        "Gender": "Female",
        "Race": "White",
        "Hair color": "Blonde",
        "Eye color": "Blue",
        "Face shape": "Oval"
    },
    {
        "name": "Larisa",
        "Gender": "Female",
        "Race": "White",
        "Hair color": "Brown",
        "Eye color": "Brown",
        "Face shape": "Oval"
    },
    {
        "name": "Matej",
        "Gender": "Male",
        "Race": "White",
        "Hair color": "Black",
        "Eye color": "Blue",
        "Face shape": "Oval"
    },
    {
        "name": "Miha",
        "Gender": "Male",
        "Race": "White",
        "Hair color": "Brown",
        "Eye color": "Green",
        "Face shape": "Square"
    }
]

def get_suspect(suspects):
    """Matches the DNA to a suspect."""
    for suspect in suspects:
        found = True
        for key, value in suspect.items():
            if key == "name":
                continue
            gene = GENES[key].get(value)
            if gene not in DNA:
                found = False
                break
        if found:
            return suspect["name"]

if __name__ == "__main__":
    print "The crimie was commited by %s" % get_suspect(SUSPECTS)
