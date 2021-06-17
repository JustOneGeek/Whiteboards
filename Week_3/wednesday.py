# Given the following list of people in our class Write a generator and use it to find the combined age of everyone in the class
my_list=[
    {"Name":"Kevin",
    "Age":36,
    "weight":220
    },
    {"Name":"Brian",
    "Age":27,
    "weight":200
    },
    {"Name":"John",
    "Age":30,
    "weight":180
    },
    {"Name":"Tony",
    "Age":23,
    "weight":150
    },
    {"Name":"David",
    "Age":24,
    "weight":150
    }
]

def my_gen_for_age(a_list):
    for person in a_list:
        yield person["Age"]

for age in my_gen_for_age(my_list):
    print(age)

def sum_age():
    return sum(my_gen_for_age(my_list))
        
    

print(sum_age())