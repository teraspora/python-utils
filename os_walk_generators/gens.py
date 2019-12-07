# Ex 1: 
import random
def randseq(start, stop, length):
    """
    Return a generator that produces a sequence of random numbers 
    of a specified length and bounds.
    """
    return (random.randrange(start, stop) for n in range(length))

print(list(randseq(0, 100, 8)))
[36, 20, 41, 87, 14, 87, 29, 52]

print(list(randseq(0, 100, 8)))
[35, 69, 67, 19, 23, 33, 62, 63, 72, 79, 78, 81, 70, 78, 3, 71, 11, 76, 4, 95]

print(list(randseq(50, 60, 5)))
[54, 50, 58, 56, 51]

# Ex 2:

def randobjects(func, length):
    """
    Return a sequence of arbitrary objects produced by successive
    invocations of a supplied function
    """
    return map(func, randseq(0, length, length))

print(list(randobjects(lambda x: x / 2, 20)))
[9.5, 9.5, 9.5, 0.5, 3.0, 3.0, 8.0, 1.5, 2.5, 3.5, 0.0, 4.0, 3.0, 3.0, 8.5, 2.5, 8.0, 0.5, 5.0, 4.5]

# Ex 3:

objs = randobjects(lambda x: x / 2, 20)
s = ':'
>>> obj_string = s.join(str(obj) for obj in objs if obj is not None)
>>> obj_string
'5.5:4.5:3.0:3.5:1.5:8.0:6.0:6.0:5.5:5.0:9.5:5.5:4.5:2.5:3.0:5.0:0.5:6.0:0.5:8.5'

# Time: 11:43, going to submit now.

# Ex. 4:

def log_objects(f, g):
    try:
        f.write(g.next)
    except StopIteration:
        f.close()