# I have a list of of all the students in class
students=["Andrew","Apollo","Cole","David","Dereck","Felix","Jessica","John", "Robert", "Saed", "Tony", "William" ]
# David and Andrew need to meet me after class
# Felix and Jessica need to do more Codewars
# Robert and William and John need to finish their homework
# and everybody else is good to go.
# Write a function that takes a students name as an argument and returns what that student needs to do.  
# Make sure to make the name argument case-insensitive
# If the person in not in the class return "Get Out of My Class"
#ex) what_to_do("David") returns: "Meet With Me After Class"
#ex) what_to_do("Joe") returns: "Get Out Of My Class"
#ex) what_to_do("Saed") returns: "You are Good to Go!"
#ex) what_to_do("felix") returns: "Do More Code Wars"
#ex) what_to_do("john") returns: "Finish your Homework"


def what_to_do(student):
    student=student.title()
    if student in students:
        if student in ["David","Andrew"]:
            return "Meet With Me After Class"
        elif student in ["Felix","Jessica"]:
            return "Do More Codewars!"
        elif student in ["Robert", "William", "John"]:
            return "Finish your Homework"
        else:
            return "You are Good to Go!"
    else:
        return "Get Out Of My CLASS!"

print(what_to_do("Saed"))