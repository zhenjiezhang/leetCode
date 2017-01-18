class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        left,right=0,len(A)-1
        

        while left<=right:
            mid=(left+right)>>1

            if A[mid]>=target:
                right=mid-1
            else:
                left=mid+1

        return left

if __name__=="__main__":
    solution=Solution()
    print solution.searchInsert([1,3,5,6], 7)
    print solution.searchInsert([1,3,5,6], 5)
    print solution.searchInsert([1,3,5,6], 2)
    print solution.searchInsert([1], 2)




