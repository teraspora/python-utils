# partitioning.py

class Klist:
    """
    A list with a key
    """
    def __init__(self, list, key):
        self.list = list
        self.key = key

def partition(arr, func):
    """
    Return a list of lists, being partitions of set(arr)
    according to the provided function.
    """
    plist = []
    keys = set(map(func, arr))
    for key in keys:
        partn = [*set([x for x in arr if func(x) == key])]
        plist.append(partn)
    return plist

from math import ceil, sqrt
primes = lambda k: [2] + sorted(partition(range(2, k), lambda n: all(n % i for i in ([2] + list(range(3, ceil(sqrt(n)) + 1, 2)))))[1])

part = lambda arr, func: [[*set([x for x in arr if func(x) == key])] for key in set(map(func, arr))]
# >>> part(primes(100), lambda n: n % 10)
# [[71, 41, 11, 61, 31], [2], [3, 73, 43, 13, 83, 53, 23], [5], [97, 67, 37, 7, 47, 17], [79, 19, 89, 59, 29]]
# >>> part(primes(100), lambda n: n // 10)
[[2, 3, 5, 7], [19, 17, 11, 13], [29, 23], [37, 31], [41, 43, 47], [59, 53], [67, 61], [73, 79, 71], [89, 83], [97]]

parts = lambda arr, func: [sorted([*set([x for x in arr if func(x) == key])]) for key in set(map(func, arr))]
