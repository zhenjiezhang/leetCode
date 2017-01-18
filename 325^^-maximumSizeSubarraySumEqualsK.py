'''325. Maximum Size Subarray Sum Equals k
Total Accepted: 3067 Total Submissions: 7867 Difficulty: Easy

Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Example 1:

Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:

Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time? 
'''
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        partialSumsDict={0:-1}
        maxL=0

        partialSum=0
        for i in xrange(len(nums)):
            partialSum+=nums[i]
            if partialSum-k in partialSumsDict:
                maxL=max(maxL, i-partialSumsDict[partialSum-k])
            if partialSum not in partialSumsDict:
                partialSumsDict[partialSum]=i
        return maxL




    def maxSubArrayLenOld(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        partialSums=[0]
        partialSumsDict={0:0}

        for i in xrange(len(nums)):
            partialSums.append(partialSums[-1]+nums[i])
            if partialSums[-1] not in partialSumsDict:
                partialSumsDict[partialSums[-1]]=i+1


        return max([j-partialSumsDict[partialSums[j]-k] for j in xrange(len(partialSums)) if partialSums[j]-k in partialSumsDict]+[0])





if __name__=="__main__":
    s=Solution()
    print s.maxSubArrayLen([1,-1,5,-2,3],3)



