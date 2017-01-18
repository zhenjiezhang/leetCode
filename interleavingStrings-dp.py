
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
    	if len(s1)+len(s2)!=len(s3):
    		return False

    	if s1=="" and s2=="" and s3=="":
    		return True

    	# if (s1=="" and s2!=s3) or (s2=="" and s1!=s3):
    	# 	return False

    	stringTable=[[False for i in range (len(s2)+1)] for j in range(len(s1)+1)]
    	stringTable[0][0]=True

    	for i in range(1,len(s1)+1):
    		if s1[i-1]==s3[i-1]:
    			stringTable[i][0]=True
    		else:
    			stringTable[i][0]=False

    	for i in range(1,len(s2)+1):
    		if s2[i-1]==s3[i-1]:
    			stringTable[0][i]=True
    		else:
    			stringTable[0][i]=False

    	for i in range(1,len(s1)+1):
    		for j in range(1,len(s2)+1):
    			if stringTable[i][j-1]==True and s2[j-1]==s3[i+j-1] or (stringTable[i-1][j]==True and s1[i-1]==s3[i+j-1]):
    				stringTable[i][j]=True

    	return stringTable[len(s1)][len(s2)]

if __name__=="__main__":

	solution=Solution()
	print solution.isInterleave("","","")
	print solution.isInterleave("aa","bb","abba")
	print solution.isInterleave("","","")
	print solution.isInterleave("aabcc","dbbca","aadbbcbcac")
	print solution.isInterleave("aabcc","dbbca","aadbbbaccc")
	print solution.isInterleave("cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc","cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc","cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc")


		







