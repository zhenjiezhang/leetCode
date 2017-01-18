'''faster:
return n > 0 and not (n & n-1)


How does this work?

bool isPowerOfTwo(int n) {
    if(n<1) return false;
    return 4294967296%n==0 ? 1: 0;
}
'''

class Solution(object):

    def isPowerOfTwo(self, n):
        return False if n==0 else (n-1)&n==0


    def isPowerOfTwoIterative(self, n):
        while n>1 and n&1==0:
            n>>=1
        return n==1


    def isPowerOfTwoOld(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
        	return False
        i=1
        while n&i==0:
        	i=i<<1

        return n|i==i

if __name__=="__main__":
	print Solution().isPowerOfTwo(4)