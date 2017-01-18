class Solution:
    # @param A, a list of integers
    # @param lower, an integer
    # @param upper, an integer
    # @return a list of strings
    def findMissingRanges(self, A, lower, upper):
        ranges=[]
        a=lower-1

        if not A or A[-1]!=upper:
        	A.append(upper+1)
        for i in xrange(len(A)):
        	if A[i]-a!=1:
        		if A[i]-a==2:
        			ranges.append(str(a+1))
        		else:
        			ranges.append(str(a+1)+'->'+str(A[i]-1))
        	a=A[i]
        return ranges

if __name__ == '__main__':
	solution=Solution()
	print solution.findMissingRanges([],1,1)
	print solution.findMissingRanges([0, 1, 3, 50, 75],0,99)


