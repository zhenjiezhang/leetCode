class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
    	if numRows==0:
    		return []
        results=[[1]]
        i=1
        while i<numRows:
        	row=[1]+[results[i-1][j]+results[i-1][j+1] for j in xrange(len(results[i-1])-1)]+[1]
        	results.append(row)
        	i+=1
        return results

if __name__=="__main__":
	print Solution().generate(5)
