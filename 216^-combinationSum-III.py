'''
216. Combination Sum III
Total Accepted: 23571 Total Submissions: 69623 Difficulty: Medium

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.

Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]


Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

'''
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.combination(k,n,range(1,10)) if n<=(18-k+1)*k/2 and k<=9 else []


    def combination(self,k,n,nums):
        if n<(nums[0]+nums[k-1])*k/2:
            return []
        if k==1:
            return [[n]] if n<10 else []

        answers=[]
        for i in xrange(len(nums)-k+1):
            next=self.combination(k-1,n-nums[i],nums[i+1:])
            answers+=[[nums[i]]+comb for comb in next]

        return answers
                


if __name__ == '__main__':
    print Solution().combinationSum3(3,9)

