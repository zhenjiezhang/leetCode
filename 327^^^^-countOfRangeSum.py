'''
327. Count of Range Sum
Total Accepted: 2516 Total Submissions: 10323 Difficulty: Hard

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i <= j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2. 
'''

from collections import defaultdict
from math import ceil, floor
import bisect
class Solution(object):

    # it is actually simpler to store partialSums in a BIT of len(max(partialSum)), but in case when max partialsum is too large, memory will be exceeded.

    def countRangeSum(self, nums, lower, upper):
        partialSums=[0]
        for n in nums:
            partialSums.append(partialSums[-1]+n)
        sortedSums=[-float('inf')]+sorted(partialSums)
        rankCount=[0]*(len(sortedSums)+1)
        # print sortedSums


        def storeCounts(rank, rankCount=rankCount, inc=1):
            # can not use bisect_left here, because the lower boundary would take this off mistakenly
            while rank<len(rankCount):
                rankCount[rank]+=inc
                rank+=rank&(-rank)

        def retrieveCount(rank, rankCount=rankCount):
            count=0
            while rank>0:
                count+=rankCount[rank]
                rank-=rank&(-rank)
            return count

        for rank in xrange(1, len(rankCount)):
            storeCounts(rank)

        count=0
        for s in partialSums:
            rank=bisect.bisect(sortedSums, s)
            storeCounts(rank, inc=-1)

            rankUpper=bisect.bisect(sortedSums, s+upper)
            rankLower=bisect.bisect_left(sortedSums, s+lower)
            # print rankLower, 'r'
            count+=retrieveCount(rankUpper)-retrieveCount(rankLower)
            # print s, rankUpper, retrieveCount(rankUpper), rankLower, retrieveCount(rankLower), count

        return count



        









    def countRangeSumSlow(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        
        partialSum=[0]
        for n in nums:
            partialSum.append(partialSum[-1]+n)

        normLower, normUpper=int(floor(lower/(1.0*upper-lower+1))), int(ceil(1.0*upper/(upper-lower+1)))

        normParticalSum=[p/(upper-lower+1) if p>=0 else int(float(p)/(upper-lower+1)) for p in partialSum]

        normParticalSumDict=defaultdict(list)
        normParticalSumDict[0].append(0)

        res=0


        for i in xrange(1,len(normParticalSum)):
            p=normParticalSum[i]

            candidate=list(normParticalSumDict[p])
            for j in xrange(normLower-1, normUpper+2):
                candidate+=normParticalSumDict[p-j]
            candidate=set(candidate)

            for c in candidate:
                if lower<= partialSum[i]-partialSum[c]<=upper:
                    res+=1
            normParticalSumDict[p].append(i)


        return res

if __name__=='__main__':
    s=Solution()
    print s.countRangeSum([-2, 5, -1], lower = -2, upper = 2)
    print s.countRangeSumSlow([-2, 5, -1], lower = -2, upper = 2)
    # print s.countRangeSum([7,-8,-1,0],-1,0)


    print s.countRangeSum([2147483647,-2147483648,-1,0],-1,0)
    print s.countRangeSumSlow([2147483647,-2147483648,-1,0],-1,0)


    print s.countRangeSum([0,-3,-3,1,1,2],3,5)
    print s.countRangeSumSlow([0,-3,-3,1,1,2],3,5)

    # print s.countRangeSum([1,2,-3,-3,-1,-3], 2, 4)
    # print s.countRangeSum([6,21,-27,17,-20,3,1,-2,10,2,23,15,-3,1,9,19,-9,-24,-30,-26,-13,23,2,-10,20,0,27,24,-28,26,0,-29,-16,0,12,-28,7,1,22,-23,20,-22,-11,7,-10,-5,27,27,0,19,-9,28,-2,6,23,-9,-9,1,8,-15],-23,-16)




            


