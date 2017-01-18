'''
38. Count and Say
Total Accepted: 66655 Total Submissions: 244493 Difficulty: Easy

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string. 
'''


class Solution:
    def nextCS(self,r):
    	result=''
    	i=0
    	while i < len(r):
    		c=r[i]
    		i+=1
    		count=1
    		while i < len(r) and r[i]==c:
    			i+=1
    			count+=1
    		result+=str(count)+str(c)

    	return result
    		




    # @return a string
    def countAndSay(self, n):
    	c=1
    	result='1'
    	while c<n:
    		result=self.nextCS(result)
    		c+=1
    	return result

if __name__ == '__main__':
	solution=Solution()
	
	print solution.countAndSay(1)
