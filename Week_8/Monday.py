# Give a string upgrade every character to the next 
#if a number increment by one if 9->0
#if letter go to next letter in alphabet
#if capital keep capitol
#if lower keep lower
# z->a
# Z->A
# 9 -> 0
#remove all other characters
# AB/c@d012&x%yzZYX^789 --> BCde123yzaAZY890

def upgrade(string):
    newstring=""
    for l in string:
        nl=ord(l)
        if 90>nl>=65 or 122> nl >= 97 or 57>nl>=48:
            newstring+=chr(nl+1)
        elif nl==90:
            newstring+=chr(65)
        elif nl==122:
            newstring+=chr(97)
        elif nl==57:
            newstring+=chr(48)
    return newstring


print(upgrade("AB/c@d012&x%yzZYX^789"))

def upgrade2(string):
    return "".join([chr(ord(l)+1) if ord(l)>=65 and ord(l)<90 or ord(l) >= 97 and ord(l)<122 or ord(l)>=48 and ord(l)<57 else chr(65) if ord(l)==90 else chr(97) if ord(l)==122 else chr(48) if ord(l)==57 else '' for l in string])
    
print(upgrade2("AB/c@d012&x%yzZYX^789"))
