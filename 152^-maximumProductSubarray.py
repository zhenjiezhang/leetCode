'''
152. Maximum Product Subarray
Total Accepted: 50097 Total Submissions: 235446 Difficulty: Medium

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6. 

this is a bit too complicated, there is much simpler ways.  I used this because I thought numbers could be floats

well, if there are floats, the calculation will be slightly different.


'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A)==1:
            return A[0]

        maxP=0
        maxProducts=[0,0]
        for i in xrange(len(A)):
            if A[i]>0:
                maxProducts=[A[i] if maxProducts[0]==0 else maxProducts[0]*A[i],\
                 0 if maxProducts[1]==0 else maxProducts[1]*A[i]]
                
            elif A[i]<0:
                maxProducts=[0 if maxProducts[1]==0 else maxProducts[1]*A[i], \
               A[i] if maxProducts[0]==0 else maxProducts[0]*A[i]]

            else:
                maxProducts=[0,0]


            if maxProducts[0]>maxP:
                maxP=maxProducts[0]

        return maxP

if __name__ == '__main__':
    solution=Solution()
    print solution.maxProduct([-4,-3,-2])
