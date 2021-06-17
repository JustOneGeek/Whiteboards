# Given an Input string (s) of all Capital Letters and a integer number (k)
# Output all the possible ways you can make a string with K letters of the input string (s)
# Return the data in an iterable of strings
# Do NOT return that same string multiple times.
# if k>len(s) then do not return an empty iterable return "invalid"
# test cases:

# print(perm("FUN",1))
# {'U', 'F', 'N'}

# print(perm("FUN",2))
# {'UN', 'NF', 'NU', 'FN', 'FU', 'UF'}

# print(perm("FUN",3))
# {'FUN', 'UFN', 'UNF', 'FNU', 'NUF', 'NFU'}

# print(perm("FUN",4))
# "invalid"

# print(perm("LOOT",4))
# {'LTOO', 'TOLO', 'OOTL', 'OTOL', 'OLOT', 'OLTO', 'TLOO', 'OOLT', 'OTLO', 'TOOL', 'LOTO', 'LOOT'}


def perm(s, k):
    from itertools import permutations
    return {"".join(s) for s in set(permutations(s,k))} or "invalid"
    



print(perm("FUN",1))
print(perm("FUN",2))
print(perm("FUN",3))
print(perm("FUN",4))
print(perm("LOOT",4))

