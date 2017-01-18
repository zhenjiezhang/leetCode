'''
186. Reverse Words in a String II
Total Accepted: 6707 Total Submissions: 22240 Difficulty: Medium

Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space? 
'''

class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        head=tail=0
        while tail<len(s):
        	while tail < len(s) and s[tail]!=' ':
        		tail+=1
        	s[head:tail]=s[head:tail][::-1]
        	tail+=1
        	head=tail
        s[:]=s[::-1]

if __name__ == '__main__':
	solution=Solution()
	print solution.reverseWords('a b')

