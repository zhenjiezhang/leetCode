'''
60. Permutation Sequence
Total Accepted: 46230 Total Submissions: 191809 Difficulty: Medium

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''
from math import factorial
class Solution:
    # @return a string

    def getPermutation(self, n, k):
        k-=1
        numbers=[i for i in xrange(1,n+1)]
        facts=[factorial(i) for i in xrange(n-1,-1,-1)]
        result=[]

        for f in facts:
            result.append(numbers[k/f])
            numbers.pop(k/f)
            k%=f
        return ''.join([`i` for i in result])







    def getPermutationOld(self, n, k):
        
        result=[i for i in xrange(1,n+1)]

        topFac=top=1
        while topFac <=k:
            top+=1
            topFac*=top

        topFac/=top


        # print top
        while k > 0:
            i=1

            while topFac*i <=k:
                if topFac*i==k:
                    # print top, topFac,i,k, result
                    tmp=result[n-top]
                    result[n-top]=result[n-top+i-1]
                    result[n-top+i-1]=tmp
                    result[n-top+1:]=sorted(result[n-top+1:])[::-1]
                    return  ''.join([str(i) for i in result])
                else:
                    i+=1

            tmp=result[n-top]
            result[n-top]=result[n-top+i-1]
            result[n-top+i-1]=tmp
            result[n-top+1:]=sorted(result[n-top+1:])

            k-=topFac*(i-1)

            topFac/=(top-1)
            top-=1
        return ''.join([str(i) for i in result])

if __name__=="__main__":
    solution=Solution()
    n=4
    # print solution.getPermutation(4,18)

    for k in xrange(1,24):
        print n,k, solution.getPermutation(n,k), solution.getPermutationOld(n,k)

