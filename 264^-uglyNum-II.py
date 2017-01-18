'''
264. Ugly Number II
Total Accepted: 22307 Total Submissions: 84998 Difficulty: Medium

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

Hint:

    The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
    An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
    The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
    Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).

    '''
from heapq import heappush, heappop, heapify, heappushpop
class Solution(object):
    # slower because heap take time, but you can adapt to any numbers
    def nthUglyNumber(self, n):
        uNums=[1]
        i=1
        heap=[(2,2,0),(3,3,0),(5,5,0)]
        heapify(heap) #(nextCandidateUglyNum, theMultiplicationNum, theIndexOfBaseUglyNumForMultiplication)
        while i<n:
            i+=1
            next=heappop(heap)
            uNums.append(next[0])
            while heap[0][0]==uNums[-1]:
                heappushpop(heap, (uNums[heap[0][2]+1]*heap[0][1], heap[0][1], heap[0][2]+1) )

            heappush(heap, (uNums[next[2]+1]*next[1], next[1], next[2]+1))
        return uNums[-1]







    def nthUglyNumberOld(self, n):
        """
        :type n: int
        :rtype: int
        """
        results=[1]
        i=1
        last2=last3=last5=0
        while i<n:
        	i+=1
        	next2val=results[last2]*2
        	next3val=results[last3]*3
        	next5val=results[last5]*5
        	results.append(min(next2val,next3val,next5val))
        	if results[-1]==next2val:
        		last2+=1
        	if results[-1]==next3val:
        		last3+=1
        	if results[-1]==next5val:
        		last5+=1

        return results[-1]

if __name__=='__main__':
	print Solution().nthUglyNumber(10)


