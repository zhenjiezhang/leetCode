# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true



class Solution:
	def isMatch(self, inString, regEx):
		lenStr=len(inString)
		lenReg=len(regEx)
		matchTable=[set() for i in range (lenReg+1)]
		matchTable[0].add(0)

		for i in range(lenReg):
			if regEx[i]=='*':
				matchTable[i+1]=set(matchTable[i])

			elif ((i==lenReg-1) or (regEx[i+1]!='*')):
				for j in matchTable[i]:
					if (j<lenStr) and (regEx[i]==inString[j]) or (regEx[i]=='.'):
						matchTable[i+1].add(j+1)

			else:
				matchTable[i+1]=set(matchTable[i])
				for j in matchTable[i]:
					inc=0
					while ((j+inc) < lenStr) and (((regEx[i]==inString[j+inc]) or (regEx[i]=='.')) and ((j+inc+1) not in matchTable[i])):
						matchTable[i+1].add(j+inc+1)
						inc=inc+1

			if (len(matchTable[i+1])==0):
				return (False)

		if lenStr in matchTable[lenReg]:
			return (True)
		else:
			return (False)

if __name__=="__main__":
	solution=Solution()
	print(solution.isMatch("aa","a"))
	print(solution.isMatch("aa","aa"))
	print(solution.isMatch("aaa","aa"))
	print(solution.isMatch("aa", "a*"))
	print(solution.isMatch("aa", ".*"))
	print(solution.isMatch("ab", ".*"))
	print(solution.isMatch("aab", "c*a*b"))
	print(solution.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
	print(solution.isMatch("ccbbabbbabababa", ".*.ba*c*c*aab.a*b*"))
	print(solution.isMatch("aaca", "ab*a*c*a"))


