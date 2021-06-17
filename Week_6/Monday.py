# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(s):
    return sum(l in 'aeiou' for l in s)

print(get_count("Hello there fine person"))
