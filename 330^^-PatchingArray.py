'''
330. Patching Array
Total Accepted: 2003 Total Submissions: 7445 Difficulty: Medium

Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.



you start from having 0.
and you extend your reach from 0.
for each num you add to your list, your max reach will be maxCurNum+num, but you may be missing numbers between your last maxCurNum and num, so you have to patch in order to make it up.
how to make it up?  at least you need to patch with maxCurNum+1, that will extend your reach, if that is not enough, repeat, until your reach goes to or beyoung num, and then add num to your reach.
or course you need to check each time you extend your reach, as you may not have to go to num, if it is larger than n.
'''
class Solution(object):

    def minPatches(self, nums, n):
        maxCurNum=0
        patch=0
        for num in nums:
            while maxCurNum+1<num:
                patch+=1
                # this step could be made faster by using log
                maxCurNum+=maxCurNum+1
                # do not forget to check here!
                if maxCurNum>=n:
                    return patch
            maxCurNum+=num
            if maxCurNum>=n:
                return patch
        while maxCurNum<n:
            patch+=1
            maxCurNum+=maxCurNum+1
        return patch




    def minPatchesMemoryError(self, nums, n):
        allNums=set(range(1,n+1))
        curNums=set([0])
        for n in nums:
            curNums|={i+n for i in curNums}
        allNums-=curNums

        patch=0
        while allNums:
            curNums|={i+min(allNums) for i in curNums}
            allNums-=curNums
            patch+=1

        return patch




if __name__=='__main__':
    s=Solution()
    print s.minPatches([1,5,10],20)

    print s.minPatches([1,2,31,33],2147483647)
