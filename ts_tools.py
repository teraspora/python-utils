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

