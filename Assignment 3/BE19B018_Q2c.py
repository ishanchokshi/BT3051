# no libraries are allowed
""" Add your functions here """
def optimal_investment_stocks_selection(price_2011, price_2021, investment_amount, n):
    """
	(list of int), (list of int), (int), (int) -> (list of int)

	>>> optimal_investment_stocks_selection([1000,1000,1800,100,1200], [3900, 1300, 4700, 120, 4500], 3000, 5)
	    [3, 0, 0, 0, 0]
	"""
    if len(price_2011) != n or len(price_2021) != n:
        raise("Incorrect Input!")
    """ Add your code here """
    profit = [x1 - x2 for (x1, x2) in zip(price_2021, price_2011)] #Calculate profit earned from each company's single share
    dp = [0 for i in range(investment_amount + 1)] #An array that will store the value of maximum profit at the index 'investment_amount'
    #If price of stock in 2011 is less than total amount, then we will either buy that stock or not buy in order to maximize the profit
    stock_buy = [-1 for i in range(investment_amount + 1)] #An array that will store which stocks were bought at the index 'investment_amount'
    n_stocks = [0] * n
    for i in range(investment_amount + 1):
        for j in range(n):
            if (price_2011[j] <= i):
                if ((dp[i - price_2011[j]] + profit[j]) > dp[i]): #If the profit earned from buying one stock of that company is more than the previous profit earned, replace the previous profit with the new profit
                    dp[i] = dp[i - price_2011[j]] + profit[j]
                    stock_buy[i] = j #Store the company serial number whose stock was bought for amount i
    amount_copy = investment_amount
    #To calculate number of stocks bought for each company:
    while (amount_copy!=0 and stock_buy[amount_copy]!=-1):
        n_stocks[stock_buy[amount_copy]] =n_stocks[stock_buy[amount_copy]] + 1
        amount_copy = amount_copy - price_2011[stock_buy[amount_copy]]
    return n_stocks