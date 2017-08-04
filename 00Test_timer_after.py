# -*- coding: utf-8 -*-

import threading

class Person(object):
    def __init__(self):
        print 'init Person'
    def speack(self):
        print 'speak'

if __name__ == '__main__':
    p = Person()
    i = 0
    while i<3:
        timer = threading.Timer(5, Person.speack, (p,))
        print 'start'
        timer.start()
        timer.join()
        print 'after join', i, '\n'
        i += 1
    i = 0