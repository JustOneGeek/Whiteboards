# Write a Python program to add the digits of a positive integer 
# repeatedly until the result has a single digit.
# The input number will be greater than 0

# EX
# Input:
n1=48
# 4+8=12
# 1+2=3
# Output:
# 3

# Input
n2=59
# Output
# 5

#recursively
def add(n):
    n_list=[int(char) for char in str(n)]
    if len(str(sum(n_list))) == 1:
        return sum(n_list)
    else:
        return add("".join([str(num) for num in str(sum(n_list))]))







#easy Math way
#Rule of the Nine out / Casting out nines
def add1(n):
    return (n-1)%9+1

print(add(n1))
print(add(n2))

print(add1(n1))
print(add1(n2))


#https://en.wikipedia.org/wiki/Casting_out_nines
