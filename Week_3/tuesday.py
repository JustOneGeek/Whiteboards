# Given the following list of people in our class use the map function 
# to sum all the age of all the people in the class
##NOTE: I do not know anyone ages or weights 
my_list=[
    {"Name":"Kevin",
    "Age":36,
    "Weight":220
    },
    {"Name":"Brian",
    "Age":27,
    "Weight":190
    },
    {"Name":"John",
    "Age":30,
    "Weight":180
    },
    {"Name":"Tony",
    "Age":23,
    "Weight":150
    },
    {"Name":"David",
    "Age":24,
    "Weight":150
    }
]
print(sum(map(lambda x: x['Age'], my_list)))