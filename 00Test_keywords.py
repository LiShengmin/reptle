#!/bin/bash

def func_a(*ps):
    for p in ps:
        print p

def func_b(func, num1):
    func(num1, num1,  4)

if __name__ == "__main__":
    func_b(func_a, 1)