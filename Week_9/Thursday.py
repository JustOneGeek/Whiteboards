
# Define a make_chocolate function that takes in (in order) small, big, goal
# The goal is the Total number of lbs of Choclate you want to recieve
# big is the number of large pieces of chocolate you have available
# big chocolate weighs 5 pounds
# small is the number of small pieces of chocolate you have available
# small chocolate weights 1 pounds
# We want to use as many large bars of chocolate as possible to reach our Goal weight
# the Function should return the number of small
# pieces of chocolate you need to use to reach your goal


def make_chocolate(small, big, goal):
    pass
  

def is_equal(qn,num1, num2):
    if num1==num2:
        print(f"Test {qn} is Correct")
    else:
        print(f"Test {qn} is Incorrect")

is_equal(1,make_chocolate(4, 1, 9), 4)
is_equal(2,make_chocolate(4, 1, 10),-1) 
is_equal(3,make_chocolate(4, 1, 7) ,2)
is_equal(4,make_chocolate(6, 2, 7) ,2)
is_equal(5,make_chocolate(4, 1, 5) ,0)
is_equal(6,make_chocolate(4, 1, 4) ,4)
is_equal(7,make_chocolate(5, 4, 9) ,4)
is_equal(8,make_chocolate(9, 3, 18),3)
is_equal(9,make_chocolate(3, 1, 9) ,-1)
is_equal(10,make_chocolate(1, 2, 7) ,-1)
is_equal(11,make_chocolate(1, 2, 6) ,1)
is_equal(12,make_chocolate(1, 2, 5) , 0)
is_equal(13,make_chocolate(6, 1, 10) ,5)
is_equal(14,make_chocolate(6, 1, 11) ,6)
is_equal(15,make_chocolate(6, 1, 12) ,-1)
is_equal(16,make_chocolate(6, 1, 13) ,-1)
is_equal(17,make_chocolate(6, 2, 10) ,0)
is_equal(18,make_chocolate(6, 2, 11) ,1)
is_equal(19,make_chocolate(6, 2, 12) ,2)
is_equal(20,make_chocolate(60, 100, 550) ,50)
is_equal(21,make_chocolate(1000, 1000000, 5000006),6) 
is_equal(22,make_chocolate(7, 1, 12) , 7)
is_equal(23,make_chocolate(7, 1, 13) , -1)
is_equal(24,make_chocolate(7, 2, 13) , 3)



#replace the empty function with answer
def make_chocolate(small, big, goal):
    num_big=goal//5
    if num_big <= big:
        left=goal-(num_big*5)

    elif num_big > big:
        left = goal-(big*5)

    if left <= small:
        return left
    else:
        return -1