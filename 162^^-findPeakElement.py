'''
162. Find Peak Element
Total Accepted: 53839 Total Submissions: 164594 Difficulty: Medium

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.
Note:

Your solution should be in logarithmic complexity.

'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if len(num)==1:
        	return 0
        elif len(num)==2:
        	return 0 if num[0]>num[1] else 1
        
        mid=len(num)/2-1
        # print len(num), mid
        if num[mid+1]<num[mid] and (mid==0 or num[mid-1]<num[mid]):
        	return mid
        elif num[mid+1]>num[mid]:
        	return mid+1+self.findPeakElement(num[mid+1:])
        else:
        	return self.findPeakElement(num[:mid])

if __name__ == '__main__':
	solution=Solution()
	print solution.findPeakElement([2,3,1,4,5,3])
	print solution.findPeakElement([4,3,2,1])

