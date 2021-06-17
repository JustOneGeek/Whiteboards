# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.
# Example 1:
# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# Example 2:
# Input: s = "odcgin", indices = [1, 2, 0, 5, 3, 4]
# Output: "coding"
# Example 3:
# Input: s = "aiohn", indices = [3,1,4,2,0]
# Output: "nihao"
# Example 4:
# Input: s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
# Output: "arigatou"
# Example 5:
# Input: s = "art", indices = [1,0,2]
# Output: "rat"

def arrange(s,i):
    answer=['']*len(s)
    for chr, idx in zip(s,i):
        answer[idx]=chr
    return "".join(answer)

print(arrange("aaiougrt",[4,0,2,6,7,3,1,5]))
