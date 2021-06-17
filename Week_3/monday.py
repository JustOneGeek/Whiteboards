# Write a Python class that defines a water glass
# When you make an instance of WaterGlass you input how full the glass is
# You can refill the glass. If you refill a full glass let the user know the glass has overflowed.
# You can take a sip of the water
# You can pour out the glass
# tTe glass can tell you how full it is
# Write some Driver code that makes a new water glass and utilizes all the methods.
class WaterGlass():
    def __init__(self, percent_full):
        self.fill_height=percent_full

    def refill(self):
        if self.fill_height >.9:
            print("You made a mess you glass over flowed")
        self.fill_height=1

    def sip(self):
        if self.fill_height>=.1:
            self.fill_height-=.1
        else:
            print("You glass is empty")

    def empty(self):
        self.fill_height=0

    def how_full(self):
        return(round(self.fill_height,1))
    @property
    def name(self):
        return("HEYYYOOOO")

#Driver Code
my_cup=WaterGlass(.5)
print(my_cup.name)
my_cup.how_full()
while my_cup.fill_height>0.1:
    my_cup.sip()
    print("I took a sip")
    print(f"My cup is now {my_cup.how_full()*100}% full")
my_cup.refill()
my_cup.refill()
my_cup.how_full()
