def replace_in_file(oldstr, newstr, file):
"""
Takes a string, a replacement string and a file path,
and replaces all occurrences of the first string with the second within the given file
"""
  with open(file) as f:
    newtxt = f.read().replace(oldstr, newstr)
  with open(file, "w") as f:
    f.write(newtxt)

import re
import collections
with open('book.txt') as file:
    words = re.findall('\w+', file.read().lower())
print(collections.Counter(words).most_common(10))