def optimal_investment_time_series(time_series):
    """
    (list of int) -> int
	
    >>> optimal_investment_time_series([3,3,0,1,2,5,2,2,4,2,7,0])
	    10
    """
    """ Add your code here """
    CP_first = float("-inf")#Setting all prices initially to negative infinity
    SP_first = float("-inf")
    CP_second = float("-inf")
    SP_second = float("-inf")
    #Profit = -(Cost Price of first stock) + (Selling price of second stock) - (Cost price of second stock) + (Selling price of second stock)
    #We can consider above formula because Cost price will always be greater than selling price else profit will be zero
    for price in time_series:
        CP_first = max(CP_first,-price) #Cost price of first stock will be minimum of price of current stock and present cost price of the first stock bought. Putting a negative sign to both in max() function will calculate this
        SP_first = max(SP_first,CP_first+price) #To check if we can sell current stock right now or later, adding the stock price and determining if we were able to maximize the first transaction.
        CP_second = max(CP_second,SP_first-price) #Cost price of second stock will be minimum of present cost price of the second stock bought and profit remaining after buying second stock. Since we are buying a stock, profit will reduce by the amount of CP of second stock
        SP_second = max(SP_second, CP_second+price) #Similar calculation for selling price of second stock. The selling price of second stock will be the maximum profit obtained.
    return SP_second