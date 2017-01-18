'''
122. Best Time to Buy and Sell Stock II
Total Accepted: 73619 Total Submissions: 180183 Difficulty: Medium

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

'''


class Solution:
    # @param prices, a list of integer
    # @return an integer
    



    def maxProfit(self, prices):

    	profit=0
    	if len(prices)>=2:
    		for i in range(1,len(prices)):
    			profit+=max(0,prices[i]-prices[i-1]) 		
    	
    	return profit


if __name__=="__main__":
	solution=Solution()
	print solution.maxProfit([1,2,1,2])
	print solution.maxProfit([1,2,1,2,-2,7,8,9,8,6,9,10])






