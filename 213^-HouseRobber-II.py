'''
213. House Robber II
Total Accepted: 20993 Total Submissions: 71410 Difficulty: Medium

Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.



similar to mine:

int rob_line(vector<int>& nums, int start, int end) {
    int odd_sum=0;
    int even_sum=0;

    for(int i=start; i<end; i++) {
        if(i%2)
            odd_sum = max(even_sum, odd_sum+nums[i]);
        else
            even_sum = max(odd_sum, even_sum+nums[i]);
    }

    return max(odd_sum, even_sum);
}

int rob(vector<int>& nums) {
    if(nums.size()==0) return 0;
    else if(nums.size()==1) return nums[0];
    else return max(rob_line(nums,0,nums.size()-1), rob_line(nums,1,nums.size()));
}


'''

class Solution(object):
    def linearRob(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]

        profits=[0 for i in xrange(len(nums))]
        profits[0]=nums[0]
        profits[1]=max(nums[:2])
        for i in xrange(2, len(nums)):
            profits[i]=max(profits[i-1],profits[i-2]+nums[i])
        return profits[-1]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)


        return max(nums[0]+self.linearRob(nums[2:-1]), self.linearRob(nums[1:]))

if __name__ == '__main__':
    print Solution().rob([1,2,1,1])
        