'''
246. Strobogrammatic Number
Total Accepted: 6432 Total Submissions: 18290 Difficulty: Easy

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
'''



class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        table=['0','1','-1','-1','-1','-1','9','-1','8','6']
        for i in xrange((len(num)+1)/2):
            if num[-i-1]!=table[ord(num[i])-48]:
                return False
        return True

if __name__ == '__main__':
    print Solution().isStrobogrammatic('8898688')
