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
    Return a list of Klist objects, being partitions of set(arr)
    according to the provided function, the keys being the set of results 
    of applying the function func to each element of arr
    """
    plist = []
    keys = set(map(func, arr))
    for key in keys:
        kl = Klist(list(set([x for x in arr if func(x) == key])), key)
        plist.append(kl)
    return plist