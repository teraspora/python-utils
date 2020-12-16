# ts_tools.py

# Some tools for working with the OS file system
# Author:  John Lynch
# November 2019

# Print directory contents
def pdc(path):
    import os
    for o in os.listdir(path):
        p = os.path.join(path, o)
        if not os.path.isdir(p):
            print(p)
        else:
            pdc(p)

# Get directory contents
def gdc(path):
    import os
    contents = []
    for o in os.listdir(path):
        p = os.path.join(path, o)
        contents.append(p if not os.path.isdir(p) else pdc(p))
    return contents


# Flatten a list
def flat(arr):
    flat_arr = []
    for el in arr:
        if not type(el) is list:
            flat_arr.append(el)
        else:
            flat_arr += flat(el)
    return flat_arr

# Some functions to flatten a nested dict
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
          4: {'name': 'Peter', 'age': '29', 'sex': {'birth':'Male', 'current': 'tapir'}, 'married': 'Yes'}}

def dlist(d):
    kvs = []
    for k,v in d.items():        
        if not isinstance(v, dict):     
            kvs.append((k, v))
        else: 
            kvs += dlist(v)
    return kvs

def dlist_ex(d, klist):
    if not klist:
        klist = ''
    kvs = []
    for k,v in d.items():        
        if not isinstance(v, dict):     
            kvs.append((f"{k}{'-' + klist if klist else ''}", v))
        else: 
            kvs += dlist_ex(v, f"{k}{'-' + klist if klist else ''}")
    return kvs

