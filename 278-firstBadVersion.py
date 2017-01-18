# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
	if version>=16:
		return True

class Solution(object):
    def firstBadVersion(self, n):
        if isBadVersion(1):
            return 1
        if n<2:
            return -1
        l=2
        r=n
        while 1<=r:
            m=(l+r)/2
            if (isBadVersion(m)) and not isBadVersion(m-1):
                return m
            elif isBadVersion(m):
                r=m-1
            else:
                l=m+1


    def firstBadVersionOld(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=0
        r=n+1
        m=(l+r)/2
        while l<r-1:
        	if m==0 and isBadVersion(m) or \
        	(m>0 and isBadVersion(m) and not isBadVersion(m-1)):
        		return m

        	if isBadVersion(m):
        		r=m+1
        	else:
        		l=m
        	m=(l+r)/2

        return m

if __name__=='__main__':
	print Solution().firstBadVersion(9732)


        