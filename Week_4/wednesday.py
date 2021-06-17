
#Given two strings, return true if they are anagrams of eachother, and false otherwise.
s1 = "anagram"
t1 = "nagaram"
# Output:
# True
s2 = "rat"
t2 = "car"
#Output:
# False

def is_anagram(s,t):
    from collections import Counter 
    return Counter(s)==Counter(t)

print(is_anagram("anagram","nagaram"))
print(is_anagram("rat","car"))




print(sorted("HEDFBGAC"))







def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return sorted(s) == sorted(t)


print(isAnagram("anagram","nagaram"))
print(isAnagram("rat","car"))