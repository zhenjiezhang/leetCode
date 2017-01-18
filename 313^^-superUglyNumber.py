'''
313. Super Ugly Number
Total Accepted: 7704 Total Submissions: 24254 Difficulty: Medium

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000. 
'''

# https://leetcode.com/discuss/72763/python-generators-on-a-heap


from heapq import heappush, heappop

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        uglies=[1]
        frontier=[]
        frontierSet=set()
        for p in primes:
            heappush(frontier, (p, p, 0)) # the result number, the prime number, and the index of basis.  (uglies[basis]*prime=result)
            frontierSet.add(p)

        for i in xrange(n-1):
            p=heappop(frontier)
            frontierSet.remove(p[0])

            uglies.append(p[0])
            newBasis=p[2]+1
            # this is very important to check!
            while p[1]*uglies[newBasis] in frontierSet:
                newBasis+=1

            heappush(frontier,((p[1]*uglies[newBasis], p[1],newBasis)))
            frontierSet.add(p[1]*uglies[newBasis])

        return uglies[-1]

if __name__ == '__main__':
    print Solution().nthSuperUglyNumber(12,[2,7,13,19])
    print Solution().nthSuperUglyNumber(0,[])





        