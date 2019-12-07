# Reverse array - equivalent to reversed(arr) or arr[::-1]
def rev(arr):
    revarr = []
    for n in range(1, len(arr) + 1):
         revarr.append(arr[-n])
    return revarr
 
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
