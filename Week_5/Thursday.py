
# Your job is to write a function which increments a string, to create a new string.
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# foo -> foo1
# foobar23 -> foobar24
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100
#
#    https://docs.python.org/3/library/stdtypes.html#string-methods

def addnumber(word):
    for i, l in enumerate(word):
        if l.isdigit():
            number = word[i:]
            w = word[:i]
            return w+str(int(number)+1).zfill(len(number))
    return word+"1"


print(addnumber("asdagaz99"))


def myFunc(string):
    if (string[-1].isdigit()):
        if (string[-1]=='9'):
            string=string[:-1]
            return myFunc(string)+"".join(["0"])
        else:
            return string[:-1]+str(int(string[-1])+1)
    else:
        return string + str(1)
print(myFunc('hello999'))