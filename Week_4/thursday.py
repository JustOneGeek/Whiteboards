##https://leetcode.com/problems/two-sum/


# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.

# Input: 
nums = [2,7,11,15]
target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Input: 
nums1 = [3,2,4]
target1 = 6
# Output: 
# [1,2]

#Input: 
nums2 = [3,3]
target2 = 6
# Output: 
# [0,1]

def two_sum(nums, target):
    d={}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target-num],i]
        d[num]=i
    return -1

print(two_sum(nums,target))
print(two_sum(nums1,target1))
print(two_sum(nums2,target2))