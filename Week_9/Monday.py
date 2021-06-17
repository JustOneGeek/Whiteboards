#Given an array of ints, return True if the numbers 1, 2, 3 appears
#  in the array somewhere.
a = [1, 1, 2, 3, 1] 
# True
b = [1, 1, 2, 4, 1] 
# False
c = [1, 1, 2, 1, 2, 3]
# True
d = [3, 4, 6, 2, 6, 1]
# True

def array123(n):
  return 1 and 2 and 3 in n




print(array123(a))
print(array123(b))
print(array123(c))
print(array123(d))