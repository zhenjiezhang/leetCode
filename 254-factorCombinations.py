class Solution(object):
    def getFactors(self, n, start=2):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result=[]

        for x in xrange(start,int(n**0.5)+1):
            if not n%x:
                result.extend([[x]+f for f in self.getFactors(n/x, start=x)+[[n/x]]])
        return result


if __name__ == '__main__':
    s=Solution()
    print s.getFactors(32)

