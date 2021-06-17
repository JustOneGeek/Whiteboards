#Write a function that prompts the user for their birth month and return there birthstone.
#If they input an invalid month tell them to try again
#Assume user inputs an integer number
stones={
    1:"Garnet",
    2:"Amethyst",
    3:"Aquamarine",
    4:"Diamond",
    5:"Emerald",
    6:"Pearl",
    7:"Ruby",
    8:"Peridot",
    9:"Sapphire",
    10:"Opal",
    11:"Topaz",
    12:"Turquoise"
}
def birthstone():
    """[A function that asks for user input as an int for the birth month and returns the birthstone as a string]

    Returns:
        [string]: [a string representing the birthstone for the inputted month]
    """
    month=0
    while 0>=month or month>12:
        month=int(input("What is your month of birth as a number? "))
        if 0>=month or month >12:
            print("Incorrect input! Try again")
    return stones[month]
print(birthstone())


def birthstone2():
    """[A function that asks for user input as an int for the birth month and returns the birthstone as a string]

    Returns:
        [string]: [a string representing the birthstone for the inputted month]
    """
    month=0
    while 0>=month or month>12:
        try:
            month=int(input("What is your month of birth as a number? "))
        except:
            print("Input must be an integer")
            month=int(input("What is your month of birth as a number? "))
        if 0>=month or month >12:
            print("Incorrect input! Try again")
    return stones[month]
print(birthstone2())