'''
46. Permutations
Total Accepted: 81660 Total Submissions: 240231 Difficulty: Medium

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1]. 
'''


'''
another interesting one
https://leetcode.com/discuss/72148/new-approach-directly-find-kth-permutation-with-simple-loop
'''


class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        self.num=num
        self.result=[]

        self.swapAll()
        return self.result

    def swapAll(self, pos=0):
        if pos==len(self.num)-1:
            self.result.append(list(self.num))
            return 

        for i in xrange(pos, len(self.num)):
            self.num[pos], self.num[i]=self.num[i], self.num[pos]
            self.swapAll(pos+1)
            self.num[pos], self.num[i]=self.num[i], self.num[pos]






if __name__=="__main__":
    solution=Solution()
    print solution.permute([1,2,3])






