'''
97. Interleaving String
Total Accepted: 43945 Total Submissions: 201365 Difficulty: Hard

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false. 
'''

'''
read my own post:

https://leetcode.com/discuss/80166/2-dp-solutions-1-quick-44-ms-the-other-slow-156-ms
'''



# time complex too high

class Solution:
    # @return a boolean

    def isInterleave(self, s1, s2, s3):

        if len(s1)+len(s2)!=len(s3):
            return False

        match=set([(0,0)]) # here 0 means including no element from s1 or s2. So (0,0) just means s1[:0] and s2[:0] form s3[:0]
                           # So (k1, k2) will mean s[:k1] and s[:k2] form s3[:k3]
        for k3 in xrange(len(s3)):
            newMatch=set()
            for m in match:
                if len(s1)>m[0] and s1[m[0]]==s3[k3]:
                    newMatch.add((m[0]+1, m[1]))
                if len(s2)>m[1] and s2[m[1]]==s3[k3]:
                    newMatch.add((m[0], m[1]+1))
            match=newMatch
        return bool(match)


    def isInterleaveSlow(self, s1, s2, s3):

    	if len(s1)+len(s2)!=len(s3):
    		return False

    	tmpBuf=[[0]*(len(s1)+1) for _ in xrange(len(s2)+1)]
        tmpBuf[0][0]=1

        for k3 in xrange(len(s3)):
            newBuf=[[0]*(len(s1)+1) for _ in xrange(len(s2)+1)]
            for k1 in xrange(max(0, k3-len(s2)), min(k3+1, len(s1))):
                if s1[k1]==s3[k3]:
                    newBuf[k3-k1][k1+1]=1 if tmpBuf[k3-k1][k1] else 0
            for k2 in xrange(max(0, k3-len(s1)), min(k3+1, len(s2))):
                if s2[k2]==s3[k3]:
                    newBuf[k2+1][k3-k2]=1 if (tmpBuf[k2][k3-k2] or newBuf[k2+1][k3-k2]) else 0
            tmpBuf=newBuf

        return bool(tmpBuf[-1][-1])




    	# for i in range(len(s3)-1,-1,-1):
    	# 	a=s3[i]
    	# 	if s1 and a==s1[-1] and (not s2 or a!=s2[-1]):
    	# 		s1=s1[:-1]
    	# 		continue
    	# 	elif s2 and a==s2[-1] and (not s1 or a!=s1[-1]):
    	# 		s2=s2[:-1]
    	# 		continue
    	# 	elif s1 and a==s1[-1] and s2 and a==s2[-1]:
    	# 		return self.isInterleave(s1[:-1],s2,s3[:i]) or self.isInterleave(s1,s2[:-1],s3[:i])

    	# 	return False

    	# return True
    # def dfs(p1=-1, p2=-1, p3=-1):


if __name__=="__main__":
	solution=Solution()
	print solution.isInterleave("","","")
	print solution.isInterleave("aa","bb","abba")
	print solution.isInterleave("","","")
	print solution.isInterleave("aabcc","dbbca","aadbbcbcac")
	print solution.isInterleave("baababbabbababbaaababbbbbbbbbbbaabaabaaaabaaabbaaabaaaababaabaaabaabbbbaabbaabaabbbbabbbababbaaaabab",\
"aababaaabbbababababaabbbababaababbababbbbabbbbbababbbabaaaaabaaabbabbaaabbababbaaaababaababbbbabbbbb",\
"babbabbabbababbaaababbbbaababbaabbbbabbbbbaaabbabaababaabaaabaabbbaaaabbabbaaaaabbabbaabaaaabbbbababbbababbabaabababbababaaaaaabbababaaabbaabbbbaaaaabbbaaabbbabbbbaaabaababbaabababbbbababbaaabbbabbbab")
	print solution.isInterleave("cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc","cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc","cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc")





