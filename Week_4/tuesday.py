# https://leetcode.com/problems/water-bottles/


def numWaterBottles(numBottles, numExchange):
    """
    :type numBottles: int
    :type numExchange: int
    :rtype: int
    """
    # I drink all the bottles I get
    drank = numBottles
    # Now I have that many empty bottles
    empties = numBottles
    
    #while I can exchange bottles:
    while empties >= numExchange:
        #I drink the bottles I get back from the exchange
        drank += empties//numExchange
        #The bottles I drank are now empty and 
        #I may have left over empty bottles from the exchange
        empties = empties//numExchange + empties % numExchange
    return drank

print(numWaterBottles(15, 4))
print(help(numWaterBottles))