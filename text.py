def func_a(*ps):
    for p in ps:
        print p

def func_b(func, num1):
    func(num1, num1,  4)

func_b(func_a, 1)


# import sys

# print '-----'

# for index in sys.path:
#     print index

# print '=================='
# print sys.argv[0]

# from sys import argv

# print argv


# from sys import path
# print path[0]

# from sys import *
# print path[0]

# print __name__

# print __version__

def po(a):
    print a

__version__= '0.0.1'


