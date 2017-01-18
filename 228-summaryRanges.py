'''
228. Summary Ranges
Total Accepted: 35817 Total Submissions: 157047 Difficulty: Easy

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"]. 

'''

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        results=[]
        if not nums:
        	return results



        l=r=0

        for i in xrange(1,len(nums)):
        	if nums[i]-nums[r]>1:
        		results.append(str(nums[l]) if l==r else '{}->{}'.format(nums[l],nums[r]))
        		l=r=i
        	else:
        		r+=1
        results.append(str(nums[l]) if l==r else '{}->{}'.format(nums[l],nums[r]))


        return results

if __name__=="__main__":
	s=Solution()
	print s.summaryRanges([0,1,2,4,5,7])
	print s.summaryRanges([])



