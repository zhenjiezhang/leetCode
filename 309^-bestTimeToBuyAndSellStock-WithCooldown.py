'''
309. Best Time to Buy and Sell Stock with Cooldown
Total Accepted: 8215 Total Submissions: 23218 Difficulty: Medium

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]

'''


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        # 4 actions: buy, sell, hold to buy
        actionResults=[-min(prices[:2]), prices[1]-prices[0], 0]

        for d in xrange(2, len(prices)):
            actionResults=[max(actionResults[0], actionResults[2]-prices[d]), actionResults[0]+prices[d], \
            max(actionResults[1], actionResults[2])]
        return max(actionResults)





    def maxProfitOld(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0

        # 4 actions: buy, sell, hold to buy, hold to sell
        actionResults=[-prices[1], prices[1]-prices[0], 0, -prices[0]]

        d=2
        while d<len(prices):
            newResults=[actionResults[2]-prices[d], max(actionResults[0], actionResults[3])+prices[d], \
            max(actionResults[1], actionResults[2]), max(actionResults[0], actionResults[3])]

            actionResults=newResults
            d+=1

        return max(actionResults)

if __name__ == '__main__':
    print Solution().maxProfit([1,4,2,7])
    print Solution().maxProfitOld([1,4,2,7])

    print Solution().maxProfit([1,2,3,0,2])
    print Solution().maxProfitOld([1,2,3,0,2])






