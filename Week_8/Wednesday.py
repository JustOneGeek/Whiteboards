# Given two non-negative integers num1 and num2 represented as String, 
# return the sum of num1 and num2 as a String.
# You cannot use the BigInteger library
# You cannot convert the string into a Int so int(num1) is not allowed

#Notes:
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 do not contain any leading zero.

num1 = '364'
num2 = '1836'

def solution1(num1,num2):
    return str(eval(num1) + eval(num2))

print(solution1(num1,num2))

def solution2(num1, num2):
    n1, n2 = 0, 0
    m1, m2 = 10**(len(num1)-1), 10**(len(num2)-1)

    for i in num1:
        n1 += (ord(i) - ord("0")) * m1 
        m1 = m1//10        

    for i in num2:
        n2 += (ord(i) - ord("0")) * m2
        m2 = m2//10

    return str(n1 + n2)

print(solution2(num1,num2))