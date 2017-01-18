class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def switch(self, num,i,j):
    	num[i]+=num[j]
    	num[j]=num[i]-num[j]
    	num[i]-=num[j]

    def nextPermutation(self, num):
    	if len(num)<2:
    		return 
        i=len(num)-2
        while i>=0 and num[i] >= num[i+1]:
        	i-=1

        if i >=0:
        	j=i+1
        	while j < len(num) and num[i] < num[j]:
        		j+=1
        	self.switch(num,i,j-1)

# you need to do this last step to make sure of smallest
        for start in xrange(i+1,(i+len(num)+1)/2):
        	self.switch(num,start,len(num)-(start-i))

solution=Solution()
print solution.nextPermutation([1])
print solution.nextPermutation([1,2,3])
print solution.nextPermutation([3,2,1])
print solution.nextPermutation([1,1,5])
print solution.nextPermutation([1,2,6,4,5,6,7])
print solution.nextPermutation([7,6,2,5,4,3,2,1])
print solution.nextPermutation([7,6,5,4,3,2,1])
print solution.nextPermutation([1,3,2])

