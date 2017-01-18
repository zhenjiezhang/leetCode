'''
229. Majority Element II
Total Accepted: 21641 Total Submissions: 86595 Difficulty: Medium

Given an integer array of size n, find all elements that appear more than floor(n/3) times. The algorithm should run in linear time and in O(1) space.
'''
class Solution(object):
    def majorityElement(self, nums):
        votes=dict()
        for n in nums:

            if n in votes:
                votes[n]+=1
            elif len(votes)<2:
                votes[n]=1

            else:
                for key in votes.keys():
                    if votes[key]==1:
                        votes.pop(key)
                    else:
                        votes[key]-=1
        # have to count again for cases like [3,2,3], count(2) is not larger than len/3
        return [v for v in votes.keys() if nums.count(v)>len(nums)/3]

if __name__=="__main__":
    print Solution().majorityElement([1,1,1,3,3,2,2,2])
    print Solution().majorityElementOld([1,1,1,3,3,2,2,2])







