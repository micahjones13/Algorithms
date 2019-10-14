#!/usr/bin/python

import sys


# this is a permuation problem, very common for interviews --- 'the amount of ways something can happen -- permutaion'
# solve this by taking in, subtracting 1, combining?
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
# n = number of cookies
# look up times for dictionaires are amazing
def eating_cookies(n, cache=None):
  # base case, if cookes is <= 0, you're done
    if n < 0:
        return 0
    elif n == 0:
        return 1
      # if used before and cacluated before, push it to cache, greater than 0 means it exits
    elif cache and cache[n] > 0:
        return cache[n]
    else:
      # he can eat 1, 2, or 3
      # call each way he can eat them recusivley, add them all together. That's how many ways he can eat them ***Permutation pattern
        if not cache:
          # initialize a chache in the range n+1
            cache = {i: 0 for i in range(n+1)}
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')


cache = {}


'''

cache = {}
def fib(n):
    global cache
    if n < 2:
        return n
    elif n in cache:
        return cache[n]
    else:
        cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]


'''
