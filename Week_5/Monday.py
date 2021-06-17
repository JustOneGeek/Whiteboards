# Given an integer return the integer with all the digits reversed:
# Must work for positive and negative numbers
# Input
x1=1234
# Output
# 4321
# Input
x2=-1234
# Output
# -4321


def reverse(x):
    if str(x)[0]!='-':
        return int(str(x)[::-1])
    else:
        return int(str(x)[1::][::-1])*-1

print(reverse(x1))
print(reverse(x2))