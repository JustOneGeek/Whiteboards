#Given a list of numbers containing one duplicate value, return the duplicated value.
# Input:
nums=[1, 2, 3, 2, 4]
# Output:
# 2

#count method
def fd(nums):
    for num in nums:
        if nums.count(num)>1:
            return num

print("Z1",fd([1, 2, 2, 3, 4]))
print("Z2",fd([3, 1, 3, 4, 2]))
print("Z3",fd([3, 1, 4, 4, 8]))

#Dictionary
def find_duplicate(nums):
    from collections import Counter
    c = Counter(nums)
    for k, v in c.items():
        if v > 1:
            return k


print("A1",find_duplicate([1, 2, 2, 3, 4]))
print("A2",find_duplicate([3, 1, 3, 4, 2]))
print("A3",find_duplicate([3, 1, 4, 4, 8]))

#Math
def find_dup(nums):
    sumnums = sum(nums)
    sumset = sum(set(nums))
    return (sumnums - sumset)


print("B1",find_dup([1, 2, 2, 3, 4]))
print("B2",find_dup([3, 1, 3, 4, 2]))
print("B3",find_dup([3, 1, 4, 4, 8]))

# If the numbers are all consecutive
# Tortoise and the Hare Algorithm
# https://davidfloyd91.github.io/floyd-tortoise-hare-cycle-linked-list-python/
def find_duplicate2(nums):
    # Find the intersection point of the two runners.
    tortoise = hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Find the "entrance" to the cycle.
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare
print("C1",find_duplicate2([1, 2, 2, 3, 4]))
print("C2",find_duplicate2([3, 1, 3, 4, 2]))
print("C3",find_duplicate2([3, 1, 4, 4, 2]))
