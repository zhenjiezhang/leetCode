'''
58. Length of Last Word
Total Accepted: 78058 Total Submissions: 275303 Difficulty: Easy

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5. 
'''
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s=s.strip()
        if len(s)==0:
            return 0
        i=len(s)-1
        while i>=0 and s[i]!=' ':
            i-=1
        return len(s)-i-1

if __name__ == '__main__':
    print Solution().lengthOfLastWord('fdfsd fsdfadsf  ')
        