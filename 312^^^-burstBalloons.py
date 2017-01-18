'''
312. Burst Balloons
Total Accepted: 5074 Total Submissions: 14935 Difficulty: Hard

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 <=n<=500, 0<=nums[i]<=100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167


Be Naive First

When I first get this problem, it is far from dynamic programming to me. I started with the most naive idea the backtracking.

We have n balloons to burst, which mean we have n steps in the game. In the i th step we have n-i balloons to burst, i = 0~n-1. Therefore we are looking at an algorithm of O(n!). Well, it is slow, probably works for n < 12 only.

Of course this is not the point to implement it. We need to identify the redundant works we did in it and try to optimize.

Well, we can find that for any balloons left the maxCoins does not depends on the balloons already bursted. This indicate that we can use memorization (top down) or dynamic programming (bottom up) for all the cases from small numbers of balloon until n balloons. How many cases are there? For k balloons there are C(n, k) cases and for each case it need to scan the k balloons to compare. The sum is quite big still. It is better than O(n!) but worse than O(2^n).

Better idea

We then think can we apply the divide and conquer technique? After all there seems to be many self similar sub problems from the previous analysis.

Well, the nature way to divide the problem is burst one balloon and separate the balloons into 2 sub sections one on the left and one one the right. However, in this problem the left and right become adjacent and have effects on the maxCoins in the future.

Then another interesting idea come up. Which is quite often seen in dp problem analysis. That is reverse thinking. Like I said the coins you get for a balloon does not depend on the balloons already burst. Therefore instead of divide the problem by the first balloon to burst, we divide the problem by the last balloon to burst.

Why is that? Because only the first and last balloons we are sure of their adjacent balloons before hand!

For the first we have nums[i-1]*nums[i]*nums[i+1] for the last we have nums[-1]*nums[i]*nums[n].

OK. Think about n balloons if i is the last one to burst, what now?

We can see that the balloons is again separated into 2 sections. But this time since the balloon i is the last balloon of all to burst, the left and right section now has well defined boundary and do not affect each other! Therefore we can do either recursive method with memoization or dp.

Final

Here comes the final solutions. Note that we put 2 balloons with 1 as boundaries and also burst all the zero balloons in the first round since they won't give any coins. The algorithm runs in O(n^3) which can be easily seen from the 3 loops in dp solution.



My complilation:

when you burst a balloon, there are two values involved.
1.  The coins returned by the balloon itself, multiplied by the present neighbors.
2.  The coins returned by the already bursted balloons that were originally between the present balloon and its present neighbors. 

When we exhaust the possible ways to burst the last balloon, we are given the present neighbors (head and tail of the present list, since we are bursting the "last" balloon), so the value 1 is easy. 
For the value 2, we can recurse on both sides.
notices that, no matter how you recurse, at any given step, you always easily compute value 1, and value 2 is always from consecutive balloons in the original list.
There is only limited number of consecutive sublist of the original list (O(N^2)), if we compute all of them, then we will save a lot of time by avoiding repeated computation for the same sublist.
This could be done with DP or with recursion.

'''
class Solution(object):
    def maxCoins(self, nums):
        nums=[1]+nums+[1]
        segDict=[[-1]*len(nums) for _ in xrange(len(nums))]
        def dfs(start, end):
            if segDict[start][end]<0:
                segDict[start][end]=max([nums[i]*nums[start-1]*nums[end+1]+dfs(start, i-1)+dfs(i+1, end) for i in xrange(start, end+1)]) if start<=end else 0
            return segDict[start][end]
        return dfs(1, len(nums)-2)

        

    def maxCoinsOld(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums=[1]+nums+[1]
        resultMatrix=[]
        resultMatrix.append([0 for i in xrange(len(nums)-1)])
        resultMatrix.append([nums[i]*nums[i-1]*nums[i+1] for i in xrange(1,len(nums)-1)])

        for length in xrange(2, len(nums)-1):
            resultMatrix.append([])
            for p1 in xrange(1,len(nums)-length):
                p2=p1+length
                maxV=0
                for i in xrange(p1,p2):
                    iValue=nums[i]*nums[p1-1]*nums[p2]+resultMatrix[i-p1][p1-1]+\
                    resultMatrix[p2-i-1][i]
                    if iValue>maxV:
                        maxV=iValue
                resultMatrix[-1].append((maxV))
        return resultMatrix[-1][0]

if __name__ == '__main__':
    print Solution().maxCoins([3,1,5,0,8])
    print Solution().maxCoinsOld([3,1,5,0,8])


