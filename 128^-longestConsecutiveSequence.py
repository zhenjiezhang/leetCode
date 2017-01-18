class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        num=set(num)
        longest=0
        while num:
        	a=num.pop()
        	up=1
        	while a+up in num:
        		num.remove(a+up)
        		up+=1
        		
        	down=1
        
        	while a-down in num:
        		num.remove(a-down)
        		down+=1
        		
        	if up+down-1>longest:
        		longest=up+down-1

        return longest

if __name__=="__main__":
	solution=Solution()
	# print solution.longestConsecutive([3,4,5,7,8,1,9,6])
	# print solution.longestConsecutive([])
	print solution.longestConsecutive([0,-1])




