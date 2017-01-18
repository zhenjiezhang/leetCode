'''
1. Two Sum
Total Accepted: 170706 Total Submissions: 848522 Difficulty: Medium

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2 
'''


class Solution:
	def twoSum(self, inputArray, targetSum):
		mapArray=dict()
		for i in range(0,len(inputArray)):
			if (targetSum-inputArray[i]) in mapArray:
				return ((mapArray[targetSum-inputArray[i]]+1,i+1))
			else:
				mapArray[inputArray[i]]=i
		return("not found")	

if __name__=="__main__":
	twoSumTest=Solution()
	print (twoSumTest.twoSum([3,2,4],6))






