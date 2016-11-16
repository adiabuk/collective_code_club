#!/usr/bin/python2

"""
Small game that generates a random number representing the floor of a
ten story building.  There is a chicken thief hiding on one of these floors,
your job is to locate the floor that the thief is hiding on before he escapes
"""

from random import randint

print "* * * Find the chicken thief * * *\n\n"

CURRENT_FLOOR = randint(0, 10)

FLOORS = ["Ground", "First", "Second", "Third", "Fourth", "Fifth", "Sixth",
          "Seventh", "Eighth", "Ninth", "Tenth"]

print "Where is the thief hiding?"

def choose_floor():
    CHOSEN_FLOOR = raw_input("Choose a floor between 0 and 10: ")
    return CHOSEN_FLOOR

CHOSEN_FLOOR = choose_floor()

while not CHOSEN_FLOOR.isdigit() or not int(CHOSEN_FLOOR) in range(0, 10):
    print "Invalid floor...."
    CHOSEN_FLOOR = choose_floor()

if int(CHOSEN_FLOOR) == CURRENT_FLOOR:
    # if the correct floor has been entered
    print "You have found the chicken thief"
else:
    # if the wrong floor has been entered
    print "You have failed the collective, the chicken thief has escaped"
    # substitute name of floor into string
    print "He was on the %s floor :-(" % FLOORS[CURRENT_FLOOR]

print "\n\n"
print "GAME OVER!"
