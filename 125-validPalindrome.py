'''
125. Valid Palindrome
Total Accepted: 84147 Total Submissions: 365296 Difficulty: Easy

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome. 
'''
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        head=0
        tail=len(s)-1
        while head<=tail:
        	while head< tail and not s[head].isalnum():
        		head+=1
        	while tail>head and not s[tail].isalnum():
        		tail-=1
        	if head <=tail:
        		if s[head].upper() != s[tail].upper():
        			return False
        	head+=1
        	tail-=1
        return True

print Solution().isPalindrome('$#@')
