'''
137. Single Number II
Total Accepted: 72734 Total Submissions: 198958 Difficulty: Medium

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 



'''


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        
        counterHigh=counterLow=0

        for i in A:
            carry=counterLow&i
            counterLow=counterLow^i
            counterHigh=counterHigh|carry
            reset=counterHigh&counterLow

            counterHigh=counterHigh&(~reset)
            counterLow=counterLow&(~reset)

        return counterLow

if __name__ == '__main__':
    solution=Solution()
    print solution.singleNumber([1])
    print solution.singleNumber([2,2,8,2,5,5,5])