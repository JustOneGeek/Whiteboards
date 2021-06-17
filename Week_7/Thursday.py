### Lets Bring It all the way back to your first assignment in this course.  
# Question #4 Asked you to determine if an input year was a leap year or not.
# Use That function to determine the days in a month given a specific year 
# taking into account leap year
# Input month as a string and year as an int
# Output the number of days in month

# Examples:
# print(month_length("march",2021))
# Outputs:
# 31
# print(month_length("april",2021))
# Outputs:
# 30
# print(month_length("february",2020))
# Outputs:
# 29
# print(month_length("february",2021))
# Outputs:
# 28
# print(month_length("february",1700))
# Outputs:
# 28
# print(month_length("february",1600))
# Outputs:
# 29
##########
### Challenge: 
## Given a Month, Day, and Year (assume int unless you want it otherwise)
## Output a String that corresponds to the correct Day of the Week (take into account leap year)
# Example:
# print(day_of_the_week(3, 31, 2021))
# Outputs:
# Wednesday
#####
## Hint:
## Zeller's Rule


def is_leap_year(a_year):
    """takes in a int for a year and returns TRUE if the year is a leap year"""
    if a_year < 0 or type(a_year) != int: raise InputError("Improper Year Format/Type")
    
    if (a_year % 4 == 0 and a_year % 100 != 0) or\
           (a_year % 4 == 0 and a_year % 100 == 0 and a_year % 400 == 0):
        return True
    else:
        return False


def month_length(month, year=None):
    """takes a string for month and returns the length of the month.
     Feb defaults to 28 days unless an int for year is added to account for leap year"""
    if type(month) != str: raise InputError("Improper Year Format/Type")
    month_30=["april", "june", "september", "november"]
    if(month.lower() in month_30):
        return 30
    elif (month.lower()=="february"):
        if year is None:
            return 28
        else:
            if(is_leap_year(year)):
                return 29
            else:
                return 28
    else:
       return 31

print(month_length("march",2021))
print(month_length("april",2021))
print(month_length("february",2020))
print(month_length("february",2021))
print(month_length("february",1700))

# https://www.geeksforgeeks.org/zellers-congruence-find-day-date/
def day_of_the_week(month,  day, year):
    """Takes a int month and a int day and int year (min year=1 else returns none) and outputs the correct day of the week as a string.  Uses Zeller's Rule"""
    #Zeller's Rule
    #F=k+ [(13*m-1)//5] +D+ [D//4] +[C//4]-2*C 
    days_map={ 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
    if not 0 < month <= 12 or type(month) !=int:  raise InputError("Improper Month Format")
    if year < 1 or type(year) !=int: raise InputError("Improper Year Format")
    if not 0 < day <=31  or type(day) !=int: raise InputError("Improper Day Format")

    C=int(str(year)[0:2])
    D=int(str(year)[2:4])
    if 1<= month <= 2: D-=1
    month = month -2 if month > 2 and month <= 12 else 12 if month == 2 else 11 if month==1 else None
    f=day+((13*month-1)//5)+D+(D//4)+(C//4)-2*C
    return(days_map[f%7])


class InputError(Exception):
    """Exception raised for errors in the input."""
    def __init__(self, message):
            self.message = message
    
print(day_of_the_week(5, 27, 2021))

    
    

    