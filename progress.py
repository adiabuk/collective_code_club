#!/usr/bin/env python2

""" Poor man's progressbar """

import sys
import time

for i in range(1, 101):
    sys.stdout.write("\r")
    sys.stdout.write("="*i + " " + str(i) + "%")
    sys.stdout.flush()
    time.sleep(0.5)
