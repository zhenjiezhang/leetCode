'''
20. Valid Parentheses
Total Accepted: 85914 Total Submissions: 306716 Difficulty: Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class Solution:
    # @return a boolean
    def isValid(self, s):
    	stack=[]
    	mapping={')':'(','}':'{',']':'['}

        pre={'(','{','['}
        post={')','}',']'}
        for c in s:
        	if c in pre:
        		stack.append(c)
        	elif c in post:
        		if stack and stack.pop()==mapping[c]:
        			continue
        		else:
        			return False

        if stack:
        	return False

        return True

if __name__ == '__main__':
	solution=Solution()
	print solution.isValid('([](({}())))')


