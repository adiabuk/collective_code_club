#!/usr/bin/env python2

""" Stdout example """

import time
import sys

sys.stdout.write("hello world!")
sys.stdout.write("\r")
sys.stdout.flush()
time.sleep(3)
sys.stdout.write("xxxxx")
