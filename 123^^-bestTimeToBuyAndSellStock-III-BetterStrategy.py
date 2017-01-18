'''
123. Best Time to Buy and Sell Stock III
Total Accepted: 49507 Total Submissions: 195189 Difficulty: Hard

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

'''
'''
my follow up, what about k transactions?
'''
class Solution:
    # @param prices, a list of integer
    # @return an integer

    def maxProfit(self, prices):
        minPriceBefore=float("inf")
        maxSingleProfit=0
        maxThreeTransactions=-float("inf")
        maxTwoProfit=0


        for day in range(len(prices)):

            minPriceBefore=prices[day] if prices[day] < minPriceBefore else minPriceBefore
            maxSingleProfit=prices[day]-minPriceBefore if prices[day]-minPriceBefore > maxSingleProfit else maxSingleProfit
            maxThreeTransactions=maxSingleProfit-prices[day] if maxSingleProfit-prices[day] > maxThreeTransactions else maxThreeTransactions
            maxTwoProfit=prices[day]+maxThreeTransactions if prices[day]+maxThreeTransactions > maxTwoProfit else maxTwoProfit


        return maxTwoProfit


if __name__=="__main__":
    solution=Solution()
    # print solution.singleMaxProfit([1,9,7,9,7,0,6,8])
    # print solution.singleMaxProfit([1,2])
    # print solution.singleMaxProfit([2,2,5])
    # print solution.singleMaxProfit([1,2,6,4,5])
    # print solution.singleMaxProfit([1,2,6,4,-1])
    # print solution.singleMaxProfit([])
    # print solution.singleMaxProfit([1,1,1,1,1,1])
    # print solution.singleMaxProfit([1,2,2,2,6,-3,-3,5])

    print solution.maxProfit([1,9,7,9,7,0,6,8])
    print solution.maxProfit([3,3,5,0,0,3,1,4])
    print solution.maxProfit([2])
    # print solution.maxProfit([1,2,6,4,5])
    # print solution.maxProfit([1,2,6,4,-1])
    # print solution.maxProfit([5,2,3,0,3,5,6,8,1,5])
    # print solution.maxProfit([1,2,4,2,5,7,2,4,9,0])
    # print solution.maxProfit([8,3,6,2,8,8,8,4,2,0,7,2,9,4,9])
    # print solution.maxProfit([1,9,6,9,1,7,1,1,5,9,9,9])
    print solution.maxProfit([3,4,6,0,3,7,5,8,2,9,1,6,6,2])


