# Function to test if a string is a palindrome, ignoring case and punctuation:

# Python 3.x (x < 8)
def isPalindrome(str):
    ss = ''.join(filter(lambda ch: ch not in ' .,;:?!-"\'', str)).lower()
    return ss == ss[::-1]

# Or in Python 3.8:
def isPalindrome(str):
    return (ss := ''.join(filter(lambda ch: ch not in ' .,;:?!-"\'', str)).lower()) == ss[::-1]