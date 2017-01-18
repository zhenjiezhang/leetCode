'''
77. Combinations
Total Accepted: 63776 Total Submissions: 194523 Difficulty: Medium

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''

'''
This is good too, but why is this faster than combineOld?

def combinations(n, k, start=1):
    if k == 1:
        return [[x,] for x in xrange(start, n+1)]

    Result = []
    for FirstNum in xrange(start, n - k + 2):
        for Comb in combinations(n, k-1, FirstNum + 1):
            Result.append([FirstNum,] + Comb)
    return Result

'''
class Solution:
    # @return a list of lists of integers

    # this DP will be much faster.  >85% >=96%
    def combine(self, n, k):
        base=[[[j] for j in xrange(1, i+1)] for i in xrange(1, n+1)]
        for height in xrange(k-1):
            newBase=[[]]
            for i in xrange(1, len(base)):
                newBase.append(newBase[-1]+[b+[height+i+1] for b in  base[i-1]])
            base=newBase[1:]
        return base[-1]





    def combineOld(self, n, k):
        
        if k==1:
            return [[i+1] for i in range(n)]
        
        return [r+[n] for r in self.combine(n-1, k-1)]+self.combine(n-1,k) if n-1>=k else [r+[n] for r in self.combine(n-1, k-1)]



if __name__=="__main__":
    solution=Solution()
    print solution.combine(4,2)
    print solution.combineOld(4,2)

