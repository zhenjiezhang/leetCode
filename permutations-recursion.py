class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
    	l=len(num)
    	output=[]
    	if l==1:
    		output.append(num)
    		return output
    	else:
    		last=num[l-1]
    		tmp=self.permute(num[0:l-1])
    		for list in tmp:
    			output.append(list+[last])
    			for i in range(len(list)):
    				output.append(list[0:i]+[last]+list[i:len(list)])
    	return output


if __name__=="__main__":
 	solution=Solution()
 	print solution.permute([1,2,3,4,5])


