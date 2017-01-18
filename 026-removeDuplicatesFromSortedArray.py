'''
26. Remove Duplicates from Sorted Array
Total Accepted: 103233 Total Submissions: 319981 Difficulty: Easy

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length. 
'''


class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A): # simple version
        A=sorted(list(set(A)))
        return len(A)

    def removeDuplicatesLinear(self, A):
        if len(A) <2:
            return len(A)

        insertionPoint, probePoint=-1, 1

        while probePoint< len(A) and A[probePoint]!=A[probePoint-1]:
            probePoint+=1

        if probePoint==len(A):
            return len(A)

        insertionPoint=probePoint
        probePoint+=1
        while probePoint< len(A):
            if A[probePoint]!=A[probePoint-1]:
                A[insertionPoint]=A[probePoint]
                insertionPoint+=1
            probePoint+=1
        A=A[:insertionPoint]
        return insertionPoint






    def removeDuplicatesOld(self, A):
        if not A:
            return 0
        if len(A)==1:
            return 1

        i=0
        n=A[i]
        ins=i+1

        while i < len(A):
            while i < len(A) and A[i]==n:
                i+=1
            if i< len(A):
                
                A[ins]=A[i]
                ins+=1
                n=A[i]
                i+=1
        A[:]=A[:ins]
        return len(A)

if __name__ == '__main__':
    solution=Solution()
    print solution.removeDuplicatesLinear([1,2,2,3,4,4,0,1])



