def maxProfit(prices):
    #Profit = -(Cost Price of first stock) + (Selling price of second stock) - (Cost price of second stock) + (Selling price of second stock)
    #We can consider above formula because Cost price will always be greater than selling price else profit will be zero
    firstBuy = float("inf") #Setting all prices initially to negative infinity
    firstSell = float("-inf")
    secondBuy =float("inf")
    secondSell = float("-inf")
    for price in prices:
        firstBuy = min(firstBuy,price) #Cost price of first stock will be minimum of current price of stock and pre
        firstSell = max(firstSell,firstBuy+price)
        secondBuy = min(secondBuy,price-firstSell)
        secondSell = max(secondSell, secondBuy+price)
    return secondSell

print(maxProfit([3,3,5,0,0,3,1,4]))
print(maxProfit([5,4,3,2,1]))