'''
32. Longest Valid Parentheses
Total Accepted: 53556 Total Submissions: 245205 Difficulty: Hard

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4. 

counting way
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use 1D DP
        # dp[i] records the longestValidParenthese EXACTLY ENDING at s[i]
        dp = [0 for x in xrange(len(s))]
        max_to_now = 0
        for i in xrange(1,len(s)):
            if s[i] == ')':
                # case 1: ()()
                if s[i-1] == '(':
                    # add nearest parentheses pairs + 2
                    dp[i] = dp[i-2] + 2
                # case 2: (()) 
                # i-dp[i-1]-1 is the index of last "(" not paired until this ")"
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    if dp[i-1] > 0: # content within current matching pair is valid 
                    # add nearest parentheses pairs + 2 + parentheses before last "("
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                    # otherwise is 0
                        dp[i] = 0
                max_to_now = max(max_to_now, dp[i])
        return max_to_now


'''

class Solution:
	#can not make it working in the counting may. the old way works fine.
	def longestValidParentheses (self, myString):
		count=0
		leftCount=0
		maxlen=0

		lastZeroCountLength=0

		for token in myString:
			if token==')':
				count-=1
			else:
				count+=1
				leftCount+=1
			if count==0:
				if maxlen<leftCount:
					maxlen=leftCount
				lastZeroCountLength=leftCount

			elif count<0:
				count=leftCount=0
				lastZeroCountLength=0

		return 2*max(maxlen,(leftCount-count-lastZeroCountLength))






	def longestValidParenthesesOld (self, myString):
		myStack=[[')',-1]]
		maxLen=0
		for i in xrange(0,len(myString)):
			if myString[i]=='(':
				myStack.append(['(',i])
			elif myString[i]==')':
				if myStack[-1][0]=='(':
					myStack.pop()
					maxLen=max(maxLen, i-myStack[-1][1])
				else:
					myStack.append([')',i])
		return maxLen


if __name__=="__main__":
	solution =Solution()
	print solution.longestValidParentheses("()))(())())(())"), solution.longestValidParenthesesOld("()))(())())(())")
	print solution.longestValidParentheses("(()(((()"), solution.longestValidParenthesesOld("(()(((()")
	print solution.longestValidParentheses("(()"), solution.longestValidParenthesesOld("(()")

