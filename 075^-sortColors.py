'''
75. Sort Colors
Total Accepted: 82264 Total Submissions: 243577 Difficulty: Medium

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
'''
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    


    def sortColors(self, A):
        l,r=0,len(A)-1
        while l<=r and A[l]==0:
            l+=1
        while r>=l and A[r]==2:
            r-=1

        w=l
        while l<=r:
            # print l, r, w
            if A[l]==1:
                l+=1
            elif A[l]==2:
                A[l], A[r]=A[r], A[l]
                r-=1
                while r>=l and A[r]==2:
                    r-=1
            else:
                A[w], A[l]=A[l], A[w]
                l+=1
                w+=1
        print A




    def sortColorsOther(self, nums):
        i = j = 0
        for k in xrange(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1


if __name__=="__main__":
    solution=Solution()
    # solution.sortColors([0,1,0,2,1])
    solution.sortColors([1,0,1,2,1,0,0,0])




