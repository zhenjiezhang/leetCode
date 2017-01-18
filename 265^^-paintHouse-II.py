'''
265. Paint House II
Total Accepted: 5103 Total Submissions: 14884 Difficulty: Hard

There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Follow up:
Could you solve it in O(nk) runtime?


using a max-heapq is O(nk), but is slower than sort, which is O(nklgk)
'''
from heapq import heappush, heappop, heappushpop, heapify

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        if len(costs)==0:
            return 0

        if len(costs)==1:
            return min(costs[0])
        currentRank=self.firstThree([(cost, index) for index, cost in enumerate(costs[0])])[:2]

        for i in xrange(1, len(costs)):
            lowestThree=self.firstThree([(cost, index) for index, cost in enumerate(costs[i])])

            currentRank=self.firstThree([min([(newCost+oldCost, newIdx) for oldCost, oldIdx in currentRank if newIdx!=oldIdx])\
             for newCost, newIdx in lowestThree]) [:2]

        return min(currentRank)[0]

    def firstThree(self, arrayOfTuples):
        '''
        using heap is slower
        '''

        result=[(float('inf'),-1) for _ in xrange(3)]

        for a in arrayOfTuples:
            for i in xrange(3):
                if a[0]<result[i][0]:
                    for j in xrange(2,i,-1):
                        result[j]=result[j-1]
                    result[i]=a
                    break

        return result







        


if __name__ == '__main__':
    solution=Solution()
    print solution.minCostII([
        [7,19,11,3,7,15,17,5,6,18,1,15,18,11],
        [13,18,18,8,13,12,11,13,4,8,2,4,5,20],
        [14,5,18,4,7,6,1,6,11,6,16,6,13,17],
        [18,17,11,3,12,4,8,6,2,7,10,9,19,3],
        [4,3,2,14,11,15,18,1,17,1,6,14,14,9],
        [9,13,15,14,5,1,1,6,11,15,16,12,10,18],
        [19,2,11,3,13,4,13,7,16,16,20,18,20,8],
        [8,19,20,9,18,13,17,1,2,4,3,20,15,9],
        [9,10,11,6,14,20,4,1,5,15,13,10,13,5],
        [13,11,9,11,9,16,3,19,1,11,6,7,12,13],
        [14,1,15,14,11,12,7,14,12,11,6,9,5,5]])

    print solution.minCostII([[4,16],[15,5],[18,17],[10,12],[14,10],[3,10],[2,11],[18,14],[9,1],[14,13]])

