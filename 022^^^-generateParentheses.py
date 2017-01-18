'''
22. Generate Parentheses
Total Accepted: 72328 Total Submissions: 207399 Difficulty: Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()" 

'''
'''
this is slow, should use a recursive method with buffering.  There are several way.
example:
https://leetcode.com/discuss/77585/java-easy-understand-recursive-dp-method-with-explanations
or :
https://leetcode.com/discuss/70441/2ms-ac-java-solution-using-recursive-call 
or my idea of inserting right p in a string of n left ps.  

or DP (best):
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]


'''
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n==1:
            return ['()']
        results=set()
        for s in self.generateParenthesis((n-1)):
            results=results | set([s[:i]+'('+s[i:j]+')'+s[j:len(s)] for i in xrange(len(s)+1) for j in xrange(i,len(s)+1)])           
        return list(results)

if __name__=="__main__":
    solution=Solution()
    print solution.generateParenthesis(3)