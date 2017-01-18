'''
45. Jump Game II
Total Accepted: 55684 Total Submissions: 225071 Difficulty: Hard

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
'''


class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):

        if len(A)==0:
            return 0
        i=0
        steps=0
        while i+A[i]+1<len(A):
            maxReach=0
            for j in xrange (i+1, i+A[i]+1):
                if j+A[j]>maxReach:
                    maxReach=j+A[j]
                    maxSecond=j
            i=maxSecond
            steps=steps+1
        return steps if i+1==len(A) else steps+1


if __name__=="__main__":
    solution=Solution()
    print solution.jump([2])



        