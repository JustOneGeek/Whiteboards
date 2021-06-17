#Make a function that takes a string and returns the most common letter in the string regardless of capitalization.
#ignore spaces
#ex) "John Loves to Play Baseball and Joanie Loves to Play Basketball, but Jenny Likes To Dance"
#output: l

s="John loves to play baseball and Joanie loves to play basketball, but Jenny like to dance"
def max_letter(sentence):
    from collections import Counter
    return max(Counter(sentence.lower().replace(" ","")),key=Counter(sentence.lower().replace(" ","")).get)
print(max_letter(s))