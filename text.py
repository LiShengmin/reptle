#!/usr/bin/env python

import sys

for index in sys.path:
    print 'index' + index

print 'sys.argv[0]' + sys.argv[0]

# from sys import argv
# print "argv" + argv

from sys import path
print "path" + path[0]

from sys import *

print 'path0' + path[0]
print '__name__   ' + __name__
# print  __version__

def po(a):
    print 'a' + a

__version__= '0.0.1'
print '__version__ ' + version
