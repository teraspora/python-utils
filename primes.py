from math import ceil, sqrt

primes = lambda k: [2] + sorted((lambda arr, func: 
    [sorted([*set([x for x in arr if func(x) == key])])
    for key in set(map(func, arr))])(range(2, k), lambda n:
    all(n % i for i in ([2] + list(range(3, ceil(sqrt(n)) + 1, 2)))))[1])

# >>> primes(100)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

