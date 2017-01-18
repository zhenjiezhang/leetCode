'''
247. Strobogrammatic Number II
Total Accepted: 5711 Total Submissions: 17516 Difficulty: Medium

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"]. 
'''

class Solution(object):
    def findStrobogrammatic(self, n, zero=False):
        if n==0:
            return [''] if zero else []
        if n==1:
            return ['1','8','0']

        validNums='0186969810' if zero else '18696981'
        return [validNums[i]+stg+validNums[-i-1] for i in xrange(len(validNums)/2) for stg in self.findStrobogrammatic(n-2, True)]

        


    def findStrobogrammaticOld(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return []
        if n==1:
            return ['0','1','8']

        center=['0','1','8'] if n%2==1 else ['']

        validNums=['0','1','6','8','9']

        results=[]

        n//=2
        totalNum=5**(n-1) #total number give the first digit

        for i in xrange(totalNum*4):
            results.append([validNums[i/(totalNum)+1]])
            digits=n-1
            newbase=i%totalNum
            remainingNum=totalNum/5


            while digits>0:
                results[-1].append(validNums[newbase/remainingNum])
                digits-=1
                newbase=i%remainingNum
                remainingNum/=5

        forReturn=[]
        for r in results:
            rightSide=r[::-1]
            for i in xrange(len(rightSide)):
                if rightSide[i]=='6' or rightSide[i]=='9':
                    rightSide[i]='9' if rightSide[i]=='6' else '6'
            for c in center:
                forReturn.append(''.join(r)+c+''.join(rightSide))

        return forReturn

if __name__ == '__main__':
    solution=Solution()
    for i in xrange(6):
        print solution.findStrobogrammatic(i)
        print solution.findStrobogrammaticOld(i)
