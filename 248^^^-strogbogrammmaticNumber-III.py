'''
254. Factor Combinations
Total Accepted: 5720 Total Submissions: 17112 Difficulty: Medium

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.

Write a function that takes an integer n and return all possible combinations of its factors.

Note:

    Each combination's factors must be sorted ascending, for example: The factors of 2 and 6 is [2, 6], not [6, 2].
    You may assume that n is always positive.
    Factors should be greater than 1 and less than n.

Examples:
input: 1
output:

[]

input: 37
output:

[]

input: 12
output:

[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]

input: 32
output:

[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]

'''

class Solution(object):








    def countDfs(self, n, zero=False):
        if n==0:
            return 0
        if n==1:
            return 3
        return (5 if zero else 4) *self.countDfs(n-2, True)


    def strobogrammaticInRange(self, low, high):
        if len(low)>len(high):
            return 0
        if len(low)==len(high):
            return len([ss for ss in self.dfs(len(low)) if ss>=low and ss<=high]) if high>=low else 0
        count=0
        count+=len([ss for ss in self.dfs(len(low)) if ss>=low])
        count+=len([ss for ss in self.dfs(len(high)) if ss<=high])
        for i in xrange(len(low)+1, len(high)):
            count+=self.countDfs(i)
        return count


    def dfs(self, n, zero=False):
        if n==0:
            return [''] if zero else []
        if n==1:
            return ['1','8','0']

        validNums='0186969810' if zero else '18696981'
        return [validNums[i]+stg+validNums[-i-1] for i in xrange(len(validNums)/2) for stg in self.dfs(n-2, True)]






    def strobogrammaticInRangeFaster(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """

        def lowerStrobs(num):
            nums=[int(c) for c in num]
            
            validStrobDigits=[0,1,6,8,9]
            strobTable=[0,1,-1,-1,-1,-1,9,-1,8,6]
            validNumsLowerThanThisIndex=[0,1,2,2,2,2,2,3,3,4]
            validNumsLowerThanThisIndex_center=[0,1,1,1,1,1,1,1,2,3]

            if len(nums)==1:
                return validNumsLowerThanThisIndex_center[nums[0]], nums[0] in [0,1,8]

            halfLength=len(nums)//2
            oddLength=len(nums)%2
            multiFactor=3 if oddLength else 1

            res=5**(halfLength)-1+validNumsLowerThanThisIndex[nums[0]]*5**(halfLength-1)*multiFactor if oddLength else \
            5**(halfLength-1)*(4+(validNumsLowerThanThisIndex[nums[0]]-1))-1

            if nums[0] not in validStrobDigits:
                return res, False

            for i, k in enumerate(nums[1:halfLength]):
                res+=5**(halfLength-i-2)*validNumsLowerThanThisIndex[k]*multiFactor
                if k not in validStrobDigits:
                    return res, False

            if oddLength:
                res+=validNumsLowerThanThisIndex_center[int(num[halfLength])]


            wholeValidStrob=False
            if not oddLength or nums[halfLength] in [0,1,8]:
                wholeValidStrob=True

                check=0
                while check < halfLength:
                    if nums[-check-1] > strobTable[nums[check]]:
                        wholeValidStrob=False
                        res+=1
                    elif nums[-check-1] < strobTable[nums[check]]:
                        wholeValidStrob=False
                        break
                    check+=1

            return res, wholeValidStrob


        highNum, highStrob=lowerStrobs(high)
        lowNum, _=lowerStrobs(low)
        return (highNum-lowNum+1 if highStrob else highNum-lowNum) if highNum>=lowNum else 0

if __name__ == '__main__':
    s=Solution()
    print s.strobogrammaticInRange("1001", "11111")
    print s.strobogrammaticInRangeFaster("1001", "11111")


    # print s.strobogrammaticInRange("0", "69")
    # print s.strobogrammaticInRange("0", "1000")
    # print s.strobogrammaticInRange("0", "96")
    # print s.strobogrammaticInRange("0", "2000")







