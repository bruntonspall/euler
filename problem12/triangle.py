import functools
import math


def triangle_number(n):
    return functools.reduce(int.__add__, range(n+1), 0)


def factors(n):
    l = [1]
    for x in range(2, int(math.floor(math.sqrt(n)))+1):
        if n % x == 0:
            l.append(x)
    return l


def find_first(n):
    i = 1
    while True:
        tri = triangle_number(i)
        if len(factors(tri)*2) >= n:
            return tri
        i += 1
