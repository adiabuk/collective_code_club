
""" Simple slow loop """

from time import sleep

MY_LIST = range(1, 101)

for item in MY_LIST:
    print "hello", item
    sleep(0.3)
