'''
80. Remove Duplicates from Sorted Array II
Total Accepted: 62889 Total Submissions: 198535 Difficulty: Medium

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length. 
'''
class Solution:
    # @param a list of integers
    # @return an integer

    def removeDuplicatesOld(self, A):
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
        return A[:insertionPoint]






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
	print solution.removeDuplicates([1,1])



