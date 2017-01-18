'''
53. Maximum Subarray
Total Accepted: 92084 Total Submissions: 258002 Difficulty: Medium

Find the contiguous subarray within an array (containing at least one number) which has the largest sum. 
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.
More practice:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


'''



'''
really nice solution:



class Solution(object):
def maxSubArray(self, nums):
    for i in xrange(1,len(nums)):nums[i]=max(nums[i], nums[i]+nums[i-1])
    return max(nums)
    '''

class Solution:
    # @param A, a list of integers
    # @return an integer






    def maxSubArray(self, A):
        i=0
        maxSum=-float('inf')


        while i < len(A):    
            maxLocal=-float('inf')
            localSum=0
            # find the first positive 
            while i< len(A) and A[i]<=0:
                if maxLocal< A[i]:
                    maxLocal=A[i]
                i+=1

            # search until this localSum no longer contribute positively
            while localSum >=0 and i < len(A):
            	localSum+=A[i]
                if maxLocal< localSum:
                    maxLocal=localSum
                i+=1
                

            if maxSum< maxLocal:
                maxSum=maxLocal
        return maxSum

if __name__=="__main__":
    solution=Solution()
    print solution.maxSubArray([1,2,3,4,5,-15,-1,4,5,19])
    print solution.maxSubArray([-3,-2,-1])
    print solution.maxSubArray([0])


