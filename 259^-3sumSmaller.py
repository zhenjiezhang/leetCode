'''
could further save time by using bisect only once for all.
'''

import bisect
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums=sorted(nums)
        c=0
        for k in xrange(len(nums)-2):
            ijTarget=target-nums[k]

            i=k+1
            j=i+bisect.bisect_left(nums[i+1:],ijTarget-nums[i])
            if j>i:
                c+=(j-i)

            if j==len(nums):
                j-=1
            while i<j-1:
                i+=1
                while i<j and nums[i]+nums[j]>=ijTarget:
                    j-=1
                if j==i:
                    break
                else:
                    c+=j-i

        return c

if __name__ == '__main__':
    s=Solution()
    print s.threeSumSmaller([-2, 0, 1, 3], 2)









        
