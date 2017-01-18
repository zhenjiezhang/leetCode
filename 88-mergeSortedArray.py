'''
88. Merge Sorted Array
Total Accepted: 82984 Total Submissions: 280557 Difficulty: Easy

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
'''
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing(void)
    def merge(self, A, m, B, n):
        p=m+n-1
        pA=m-1
        pB=n-1
        while pA>=0 and pB>=0:
            if A[pA]>B[pB]:
                A[p]=A[pA]
                pA-=1
            else:
                A[p]=B[pB]
                pB-=1
            p-=1

        if pA<0:
            A[:pB+1]=B[:pB+1]

A=[1,3,6,0,0,]
B=[2,4]
Solution().merge(A,3,B,2)
print A

