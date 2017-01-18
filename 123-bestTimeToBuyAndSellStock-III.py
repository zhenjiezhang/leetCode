'''
123. Best Time to Buy and Sell Stock III
Total Accepted: 49507 Total Submissions: 195189 Difficulty: Hard

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


'''
# # should be much shorter!

# public class Solution {
#     public int maxProfit(int[] prices) {
#         int hold1 = Integer.MIN_VALUE, hold2 = Integer.MIN_VALUE;
#         int release1 = 0, release2 = 0;
#         for(int i:prices){                              // Assume we only have 0 money at first
#             release2 = Math.max(release2, hold2+i);     // The maximum if we've just sold 2nd stock so far.
#             hold2    = Math.max(hold2,    release1-i);  // The maximum if we've just buy  2nd stock so far.
#             release1 = Math.max(release1, hold1+i);     // The maximum if we've just sold 1nd stock so far.
#             hold1    = Math.max(hold1,    -i);          // The maximum if we've just buy  1st stock so far. 
#         }
#         return release2; ///Since release1 is initiated as 0, so release2 will always higher than release1.
#     }
# }

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def singleMaxProfit(self,prices):
        profit=0
        lowest=float("inf")
        peak=-1
        trough=-1
        tmpTrough=-1
        if len(prices)>1:
            for p in range(len(prices)):
                if prices[p]<lowest:
                    lowest=prices[p]
                    tmpTrough=p
                elif prices[p]-lowest>profit:
                    profit=prices[p]-lowest
                    peak=p
                    trough=tmpTrough
                    

        return profit


    def maxProfit(self, prices):
        profit=0
        peaks=[]
        troughs=[]


        if len(prices)>1:
            
            if len(prices)>3:
                if (prices[1]>prices[0]):
                    troughs.append(0)
                for i in range(1,len(prices)-1):
                    if prices[i]>=prices[i-1] and prices [i]>prices[i+1] and troughs and (not peaks or troughs[len(troughs)-1]>peaks[len(peaks)-1]):
                        peaks.append(i)
                    elif prices[i]<=prices[i-1] and prices[i]<prices[i+1] and ((not troughs) or (peaks and peaks[len(peaks)-1] > troughs[len(troughs)-1])):
                        troughs.append(i)
                if (prices[len(prices)-1]>prices[len(prices)-2]):
                    peaks.append(len(prices)-1)

                if prices[len(prices)-1]==prices[len(prices)-2]:
                    i=len(prices)-2
                    while i>0 and prices[i]==prices[i-1]:
                        i-=1

                    if i>0 and prices[i]>prices[i-1]:
                        peaks.append(len(prices)-1)


            else:
                profit=self.singleMaxProfit(prices)
                return profit

            if len(peaks)>=2:
                firstBuy=troughs[0]
                firstSell=peaks[0]
                secondBuy=troughs[1]
                secondSell=peaks[1]



                
                firstProfit=prices[peaks[0]]-prices[troughs[0]]
                secondProfit=prices[peaks[1]]-prices[troughs[1]]

                profit=firstProfit+secondProfit

                # print troughs, peaks

                if len(peaks)==2:
                    return profit

                lowest=troughs[2]

                for peak in range(2,len(peaks)):
                    if prices[troughs[peak]]<=prices[lowest]:
                        lowest=troughs[peak]


                    thirdProfit=prices[peaks[peak]]-prices[lowest]
                    jointFirstProfit=max(firstProfit,secondProfit,prices[secondSell]-prices[firstBuy])

                    newSecondProfit=prices[peaks[peak]]-prices[secondBuy]

                    oldProfit=profit
                    newProfit1=thirdProfit+jointFirstProfit
                    newProfit2=newSecondProfit+firstProfit

                    
                    # print firstProfit,secondProfit
                    # print newSecondProfit
                    # print oldProfit,newProfit1,newProfit2

                    profit=max(oldProfit,newProfit1,newProfit2)

                    if profit==newProfit2:
                        secondSell=peaks[peak]
                        secondProfit=prices[secondSell]-prices[secondBuy]
                        if len(troughs) >  peak+1:
                            lowest=troughs[peak+1]

                    elif profit==newProfit1:
                        if jointFirstProfit==secondProfit:
                            firstBuy=secondBuy
                            firstSell=secondSell
                            firstProfit=prices[firstSell]-prices[firstBuy]

                        elif jointFirstProfit==prices[secondSell]-prices[firstBuy]:
                            firstSell=secondSell
                            firstProfit=prices[firstSell]-prices[firstBuy]

                        secondBuy=lowest
                        secondSell=peaks[peak]
                        secondProfit=prices[secondSell]-prices[secondBuy]
                        if len(troughs) >  peak+1:
                            lowest=troughs[peak+1]

                    # print "summary",firstBuy,firstSell,secondBuy,secondSell, profit, prices[firstSell]-prices[firstBuy]+prices[secondSell]-prices[secondBuy]
# 



            else:
                profit=self.singleMaxProfit(prices)
                return profit



        return profit




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
    # print solution.maxProfit([2,2,5])
    # print solution.maxProfit([1,2,6,4,5])
    # print solution.maxProfit([1,2,6,4,-1])
    # print solution.maxProfit([5,2,3,0,3,5,6,8,1,5])
    # print solution.maxProfit([1,2,4,2,5,7,2,4,9,0])
    # print solution.maxProfit([8,3,6,2,8,8,8,4,2,0,7,2,9,4,9])
    # print solution.maxProfit([1,9,6,9,1,7,1,1,5,9,9,9])
    print solution.maxProfit([3,4,6,0,3,7,5,8,2,9,1,6,6,2])
