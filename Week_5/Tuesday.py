#Given a string return True if the string can be rearranged to make a palindrome
#a palindrome can be spelled the same forwards and backwards

# Input
s1="aabbcc"
# Output
# True

# Input
s2="aabebcc"
# Output
# True

# Input
s3="racecar"
# Output
# True

# Input
s4="abcd"
# Output
# False

# Input
s5="aaabbbcc"
# Output
# False

import collections
def is_palidrome(str):
    cnts=collections.Counter(str)
    only1=True
    for v in cnts.values():
        if v % 2 != 0 and only1:
            only1=False
        elif v % 2 != 0:
            return False
    return True

print(is_palidrome(s1))
print(is_palidrome(s2))
print(is_palidrome(s3))
print(is_palidrome(s4))
print(is_palidrome(s5))



#Better Solutions:
#https://www.geeksforgeeks.org/check-characters-given-string-can-rearranged-form-palindrome/