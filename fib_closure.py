#!/usr/bin/env python
# coding: utf-8

'''

Fibonacci

    >>> fib(4)
    5

'''

import time

def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

def memoize(fn):
    memo = {}
    def memoizer(*param1):
        key = repr(param1)
        if not key in memo:
            memo[key] = fn(*param1)
        return memo[key]
    return memoizer

fib = memoize(fib)
t1 = time.time()
for vezes in range(30):
    fib(vezes)
t2 = time.time()

print 'Tempo: %2.5fs' % (t2-t1)

