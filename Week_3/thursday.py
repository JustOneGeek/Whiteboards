# # O(n) time
# # start with a list of 100 elements

# my_list = list(range(100))
# # Loop through it once
# for i in my_list:
#     if i ==0: #Best Case @i=0 so 0(1) time
#         print(f"i: {i} total print statements: {i}")
#         break
# # we get 100 loops from a list of len 100 so n time


# # O(n**2) time
# # start with a list of 100 elements
# my_list = list(range(100))
# # Loop through it twice (as this would be the worse case scenario)
# num_of_prints = 0
# for i in my_list:
#     for j in my_list:
#         if i ==0 or j==0: #Best Case @i=0 so 0(1) time
#             print(f"i: {i} j: {j} total print statements: {num_of_prints:,}")
#             num_of_prints += 1
# # We get 100**2 iterations 10,000 so n**2 time

# times_through_loop = []
# my_list = list(range(1000))


# def nlogn(lst, times_through_loop, i):
#     while len(lst) > 1:
#         times_through_loop.append(i)
#         i += 1
#         nlogn(lst[len(lst)//2:-1], times_through_loop, i)
#         nlogn(lst[0:len(lst)//2], times_through_loop, i)
#         return


# nlogn(my_list, times_through_loop, i := 1)
# print(f"This is the {max(times_through_loop)} times through the loop")
# # nlog2(n) 100 log2(100)=6.6


# Implement a function that receives a string, and lets you extend it with repeated calls. When no argument is passed you should return a string consisting of space-separated words you've received earlier.

# Note: there will always be at least 1 string; all inputs will be non-empty.

# For example:

# create_message("Hello")("World!")("how")("are")("you?")() == "Hello World! how are you?"


def create_message(s):
    strings = []
    def _msg(string=None):
        if string is None:
            return " ".join(strings)
        strings.append(string)
        return _msg

    return _msg(s)

print(create_message("Hello")("World!")("how")("are")("you?")())
