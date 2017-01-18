'''
279. Perfect Squares
Total Accepted: 24480 Total Submissions: 78493 Difficulty: Medium

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9. 


http://mathoverflow.net/questions/29644/enumerating-ways-to-decompose-an-integer-into-the-sum-of-two-squares
'''


class Solution(object):
    def __init__(self):
        self.cache={}


    def numSquares(self, n):# do not know why this TLE while other C++ versions did not
        results=[0,1]
        if n<2:
            return results[n]
        for i in xrange(2,n+1):

            results.append(1+min([results[i-t*t] for t in xrange(int(i**0.5)/2+1,int(i**0.5)+1)]))
        return results[-1]



    def numSquaresOld(self, n):
        """
        :type n: int
        :rtype: int
        """
        top=n**.5

        if top==int(top):
            return 1

        minNum=float('inf')
        
        for i in xrange(int(top),int(top)/2,-1):
            res=n-i*i
            if res not in self.cache:
                subnum=self.numSquares(res)
                self.cache[res]=subnum
            else:
                subnum=self.cache[res]

            if subnum<minNum:
                minNum=subnum

        return minNum+1

'''
below is faster too
'''
import math
cache = {}
class Solution_faster:
    global cache
    def r(self, n):
        return range(int(math.sqrt(n)),int(math.sqrt(n))/2,-1)    
        # helper function which returns a list [1 to sqrt(n)]

    def numSquares(self, i):
        if i == 0:
            return 0

        if i in cache:
            return cache[i]
        else:
            answer = 1 + min([self.numSquares(i - cj * cj) for cj in self.r(i)]) 
            cache[i] = answer
            return answer


'''
this is still pretty slow, take the same idea to dp will be faster
with the cache, the time complexity should be the same to dp, the extra expense is in the function calling

'''
if __name__=='__main__':
    print Solution().numSquares(9542)


        