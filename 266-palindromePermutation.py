'''
266. Palindrome Permutation
Total Accepted: 7836 Total Submissions: 15832 Difficulty: Easy

Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True. 


'''

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        letterCounts=[0]*128
        for c in s:
            ic=ord(c)
            letterCounts[ic]=0 if letterCounts[ic] else 1
        return sum(letterCounts)<=1

if __name__ == '__main__':
    print Solution().canPermutePalindrome('kkjj')