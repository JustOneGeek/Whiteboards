# The question asks the following: Write a function that takes an integer flight_length
#  (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean
#  indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
movie_lengths1=[20, 30, 110, 40, 50] #true
movie_lengths2=[80, 110, 40]  #false
flight_length=160
#Set
def flight_plan_complete (flight_length, movie_lengths):
    myset=set()
    for i in movie_lengths:
        if flight_length-i in myset:
            return True
        myset.add(i)
    return False
    
print("output",flight_plan_complete(flight_length, movie_lengths1))
print("output",flight_plan_complete(flight_length, movie_lengths2))

#Dict
def flight_plan_complete2 (flight_length, movie_lengths):
    mydict={}
    for i in range(len(movie_lengths)):
        remainder = flight_length - movie_lengths[i]
        if mydict.get(remainder):
            return True
        mydict[movie_lengths[i]]=i
    return False

print("output2",flight_plan_complete2(flight_length, movie_lengths1))
print("output2",flight_plan_complete2(flight_length, movie_lengths2))    

#TOO SLOW
def flight_plan_complete3 (flight_length, movie_lengths):
    for i in movie_lengths:
        for j in movie_lengths:
            if i + j == flight_length:
                return True
    return False

# Also too slow.  for in with a list is looping over all the values
def flight_plan_complete4 (flight_length, movie_lengths):
    for i in movie_lengths:
        if i - flight_length in movie_lengths:
            return True
    return False
