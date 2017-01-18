'''
69. Sqrt(x)
Total Accepted: 79074 Total Submissions: 324168 Difficulty: Medium

Implement int sqrt(int x).

Compute and return the square root of x.
'''
#Isaac Newton

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
    	algMean=(1.0+x)/2
    	algMeanSup=x/algMean
    	while algMean-algMeanSup > 0.00001:
    		algMean=(algMean+algMeanSup)/2
    		algMeanSup=x/algMean
    	# print algMeanSup,algMean 
    	return int (algMean)

if __name__=="__main__":

	solution=Solution()
	print solution.sqrt(3)
	print solution.sqrt(5)

        