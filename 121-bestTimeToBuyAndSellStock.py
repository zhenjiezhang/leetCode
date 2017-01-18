'''
121. Best Time to Buy and Sell Stock
Total Accepted: 81820 Total Submissions: 234998 Difficulty: Medium

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''
# could be much shorter!!!!
#  votes
# 43 views

# int maxProfit(vector<int> &prices) {
#     int maxPro = 0;
#     int minPrice = INT_MAX;
#     for(int i = 0; i < prices.size(); i++){
#         minPrice = min(minPrice, prices[i]);
#         maxPro = max(maxPro, prices[i] - minPrice);
#     }
#     return maxPro;
# }


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        buyP=float('inf')
        profit=0

        for p in prices:
            if p<buyP:
                buyP=p
            elif p-buyP>profit:
                profit=p-buyP
        return profit





    def maxProfitOldWhatTheHell(self, prices):

    	if len(prices)<2:
    		return 0

    	troughs=[]
    	peaks=[]
    	profit=0

    	if prices[0]<=prices[1]:
    		troughs.append(0)

    	for i in range(1,len(prices)-1):
    		if prices[i] < prices[i-1] and prices[i] <= prices [i+1]:
    			troughs.append(i)
    		if prices[i] > prices[i-1] and prices[i]>=prices[i+1]:
    			peaks.append(i)

    	if prices[len(prices)-1] > prices[len(prices)-2]:
    		peaks.append(len(prices)-1)


    	if not troughs:
    		return profit

    	maxPeakDay=-1

    	for troughDay in troughs:
    		if troughDay>maxPeakDay:
    			# print troughDay
    			for peakDay in peaks:
    				if peakDay>troughDay and prices[peakDay]-prices[troughDay]>profit:
    					profit=prices[peakDay]-prices[troughDay]
    					maxPeakDay=peakDay
    		else:
    			if prices[maxPeakDay]-prices[troughDay] > profit:
    				profit=prices[maxPeakDay]-prices[troughDay]

    	return profit


if __name__=="__main__":
	solution=Solution()
	print solution.maxProfit([1,9,7,9,7,0,6,8])
	# print solution.maxProfit([1,2])
	# print solution.maxProfit([2,2,5])
	# print solution.maxProfit([1,2,6,4,5])
	# print solution.maxProfit([1,2,6,4,-1])
	# print solution.maxProfit([])
	# print solution.maxProfit([1,1,1,1,1,1])
	# print solution.maxProfit([1,2,2,2,6,-3,-3,5])



