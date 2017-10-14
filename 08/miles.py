#! /usr/bin/env python2
# -*- coding: utf-8 -*- 
def main():
    nautic = raw_input("Če te zanimajo navtične milije, napiši 'arr': ")
    pirate = True if nautic == "arr" else False
    conversion = 0.539956803 if pirate else 0.539956803
    unit = "navtičnih milj" if pirate else "milj"
    while True:
        distance = raw_input("Vnesi število kilometorv: ")
        try:
            distance = int(distance)
            to_miles = distance * conversion
            break
        except ValueError:
            print "Vnesi število, ne pa %s" % distance
    print "{} km je {} {}".format(distance, to_miles, unit)
    if pirate:
        print "............ arrrrrrr!"

if __name__ == "__main__":
    print "Pozdravljen! Sem program za pretvarjanje kilometrov v milije."
    while True:
        main()
        quit = raw_input("Če želiš še kaj pretvorit, napiši 'da': ")
        if not quit.lower() == "da":
            break
