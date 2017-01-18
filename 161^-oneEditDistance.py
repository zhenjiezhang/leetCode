'''
161. One Edit Distance
Total Accepted: 8764 Total Submissions: 32150 Difficulty: Medium

Given two strings S and T, determine if they are both one edit distance apart.
'''
class Solution:
    # @param s, a string
    # @param t, a string
    # @return a boolean

    '''
    Another way, but I don't think it is faster than mine.
    
    def isOneEditDistance(self, s, t):
        n, m = len(s), len(t)
        if abs(n - m) > 1:
            return False
        k = min(n, m)
        i = j = 0
        while i < k and s[i] == t[i]:
            i += 1
        while j < k - i and s[~j] == t[~j]:
            j += 1
        return max(n, m) - (i + j) == 1
    '''

    def isOneEditDistance(self, s, t):
    	if abs(len(s)-len(t))>1:
    		return False
    		
        if len(s)==len(t):
            if s==t:
                return False
            for i in xrange(len(s)):
                if s[i]!=t[i]:
                    return s[i+1:]==t[i+1:]
            

        else:
            if (s==t[:-1] if len(s)<len(t) else t==s[:-1]):
                return True
            
            for i in xrange(len(s) if len(s)<len(t) else len(t)):
                if s[i]!=t[i]:
                    return s[i:]==t[i+1:] if len(s)<len(t) else s[i+1:]==t[i:]


if __name__ == '__main__':
    solution=Solution()
    print solution.isOneEditDistance('abcdde','abcdd')
    print solution.isOneEditDistance('','')
