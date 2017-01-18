'''
39. Combination Sum
Total Accepted: 74861 Total Submissions: 253061 Difficulty: Medium

Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
    The solution set must not contain duplicate combinations.

For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
'''

import bisect

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers

    
    def combinationSum(self, candidates, target, sort=True):
        if sort:
            candidates=sorted(set(candidates))

        candidates=candidates[:bisect.bisect(candidates, target)]
        limit=bisect.bisect(candidates, target/2)
        
        results=[[target]] if candidates and candidates[-1]==target else []
        for i in xrange(limit):
            results+=([[candidates[i]]+l for l in self.combinationSum(candidates[i:], target-candidates[i], sort=False)])

        return results






    def combinationSumOld(self, candidates, target):
        if not candidates:
            return []

        candidates=sorted(candidates)
        index=bisect.bisect(candidates, target)
        if index==0:
            return []
        

        results=[]

        last=candidates[index-1]
        while (last <= target):
            preResults=self.combinationSum(candidates[:index-1],target-last) 
            for result in preResults:
                result+=[candidates[index-1] for i in xrange(last/candidates[index-1])]
            results+=preResults
            last+=candidates[index-1]

        results+=self.combinationSum(candidates[:index-1],target)

        if target%candidates[index-1]==0:
            results.append([candidates[index-1] for i in xrange(target/candidates[index-1])])


        return [list(i) for i in set([tuple(result) for result in results])]


            



if __name__=="__main__":
    solution=Solution()
    print solution.combinationSum([1,2,3,5,2],5)