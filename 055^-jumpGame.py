'''
55. Jump Game
Total Accepted: 66138 Total Submissions: 239486 Difficulty: Medium

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false. 
'''


class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        dist=len(A)-1
        if dist<=0:
        	return True
        
        pos=0
        reach=0
        while pos <=reach:
        	reach=max(reach,pos+A[pos])
        	pos+=1
        	if reach>=dist:
        		return True
        return False

if __name__=="__main__":
	print Solution().canJump([2,3,1,1,4])
	print Solution().canJump([3,2,1,0,4])
