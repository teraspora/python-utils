def store():
    ostore = []
    def store_object(obj):
        ostore.append(obj)
    def get_store():
        return ostore
    def clear():
        ostore.clear()
    return store_object, get_store, clear, lambda: len(ostore)


store_thing, get_store, clear_store, store_size = store()

# pickle an object

import pickle
with open('test_obj.pk', 'wb') as f:
    pickle.dump(o, f)

with open('../python/python-utils/test_obj.pk', 'rb') as f:
    m = pickle.load(f)

# pickle.dumps(obj, protocol=None, *, fix_imports=True, buffer_callback=None)
# Return the pickled representation of the object obj as a bytes object, instead of writing it to a file.

# pickle.loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None)
# Return the reconstituted object hierarchy of the pickled representation bytes_object of an object.

# https://docs.python.org/3.8/library/pickle.html#pickle.Pickler

# What can be pickled and unpickled?
# The following types can be pickled:

# None, True, and False

# integers, floating point numbers, complex numbers

# strings, bytes, bytearrays

# tuples, lists, sets, and dictionaries containing only picklable objects

# functions defined at the top level of a module (using def, not lambda)

# built-in functions defined at the top level of a module

# classes that are defined at the top level of a module

# instances of such classes whose __dict__ or the result of calling __getstate__() is picklable (see section Pickling Class Instances for details).

# Attempts to pickle unpicklable objects will raise the PicklingError exception; when this happens, an unspecified number of bytes may have already been written to the underlying file. Trying to pickle a highly recursive data structure may exceed the maximum recursion depth, a RecursionError will be raised in this case. You can carefully raise this limit with sys.setrecursionlimit().

# Note that functions (built-in and user-defined) are pickled by “fully qualified” name reference, not by value. 2 This means that only the function name is pickled, along with the name of the module the function is defined in. Neither the function’s code, nor any of its function attributes are pickled. Thus the defining module must be importable in the unpickling environment, and the module must contain the named object, otherwise an exception will be raised. 3

# Similarly, classes are pickled by named reference, so the same restrictions in the unpickling environment apply. Note that none of the class’s code or data is pickled, so in the following example the class attribute attr is not restored in the unpickling environment:

# class Foo:
#     attr = 'A class attribute'

# picklestring = pickle.dumps(Foo)
# These restrictions are why picklable functions and classes must be defined in the top level of a module.

# Similarly, when class instances are pickled, their class’s code and data are not pickled along with them. Only the instance data are pickled. This is done on purpose, so you can fix bugs in a class or add methods to the class and still load objects that were created with an earlier version of the class. If you plan to have long-lived objects that will see many versions of a class, it may be worthwhile to put a version number in the objects so that suitable conversions can be made by the class’s __setstate__() method.

# Math

>>> from math import *
>>> isqrt(67108864)
8192
>>> isqrt(67109099)
8192
>>> comb(6,4)   # comb(n, m) = n! / (m!(1-m)!)
15
>>> perm(6,4)
360
>>> comb(8,3)
56
>>> dist((2,3),(7,15))
13.0
>>> 
>>> frexp(1536)
(0.75, 11)
>>> frexp(1267650600228229401496703205376)
(0.5, 101)
>>> gcd(10206, 5040)
126
>>> gamma(-3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
>>> gamma(-3.7)
0.25164399590242265
>>> tau
6.283185307179586
>>> 
functools.partial(func, /, *args, **keywords)
# Return a new partial object which when called will behave like func called with the positional arguments args and keyword arguments keywords. If more arguments are supplied to the call, they are appended to args. If additional keyword arguments are supplied, they extend and override keywords.
>>> from functools import partial
>>> basetwo = partial(int, base=2)
>>> basetwo.__doc__ = 'Convert base 2 string to an int.'
>>> basetwo('10010')
18

class functools.partialmethod(func, /, *args, **keywords)
Return a new partialmethod descriptor which behaves like partial except that it is designed to be used as a method definition rather than being directly callable.

func must be a descriptor or a callable (objects which are both, like normal functions, are handled as descriptors).

When func is a descriptor (such as a normal Python function, classmethod(), staticmethod(), abstractmethod() or another instance of partialmethod), calls to __get__ are delegated to the underlying descriptor, and an appropriate partial object returned as the result.

When func is a non-descriptor callable, an appropriate bound method is created dynamically. This behaves like a normal Python function when used as a method: the self argument will be inserted as the first positional argument, even before the args and keywords supplied to the partialmethod constructor.

Example:
>>> class Cell(object):
...     def __init__(self):
...         self._alive = False
...     @property
...     def alive(self):
...         return self._alive
...     def set_state(self, state):
...         self._alive = bool(state)
...     set_alive = partialmethod(set_state, True)
...     set_dead = partialmethod(set_state, False)
...
>>> c = Cell()
>>> c.alive
False
>>> c.set_alive()
>>> c.alive
True