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
