'''
28. Implement strStr()
Total Accepted: 85678 Total Submissions: 360526 Difficulty: Easy

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. 


Not required, but you can use KMP:
https://leetcode.com/discuss/73278/kmp-in-c-explanation-included
'''


class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if len(haystack)<len(needle):
        	return -1

        for i in xrange(len(haystack)-len(needle)+1):
        	if haystack[i:i+len(needle)]=needle:
        		return i
        return -1