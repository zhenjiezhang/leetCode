'''
16. 3Sum Closest
Total Accepted: 62706 Total Submissions: 223822 Difficulty: Medium

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num=sorted(num)
        # print num, target
        gap=float('inf')

        for i in xrange(0,len(num)-2):
            left=i+1
            right=len(num)-1

            twoSumTarget=target-num[i]

            while (left!=right):
                twoSum=num[left]+num[right]
                newGap=abs(twoSum-twoSumTarget)

                if twoSum==twoSumTarget:
                    return target
                elif twoSum<twoSumTarget:
                    left+=1
                else:
                    right-=1
                if  gap>newGap:
                    gap=newGap
                    result=twoSum+num[i]

        return result

if __name__=="__main__":
    solution=Solution()
    print solution.threeSumClosest([-1,2,0,-4],2)
    print solution.threeSumClosest([1,1,1,0],-100)


