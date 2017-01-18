'''
10. Regular Expression Matching
Total Accepted: 66605 Total Submissions: 312321 Difficulty: Hard

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") to false
isMatch("aa","aa") to true
isMatch("aaa","aa") to false
isMatch("aa", "a*") to true
isMatch("aa", ".*") to true
isMatch("ab", ".*") to true
isMatch("aab", "c*a*b") to true
'''


'''
you can convert this recursive into dp, will be faster.
public boolean isMatch(String s, String p) {
    int sL=s.length(), pL=p.length();

    boolean[][] dp = new boolean[sL+1][pL+1];
    dp[0][0] = true; // If s and p are "", isMathch() returns true;

    for(int i=0; i<=sL; i++) {

        // j starts from 1, since dp[i][0] is false when i!=0;
        for(int j=1; j<=pL; j++) {
            char c = p.charAt(j-1);

            if(c != '*') {
                // The last character of s and p should match;
                // And, dp[i-1][j-1] is true;
                dp[i][j] = i>0 && dp[i-1][j-1] && (c=='.' || c==s.charAt(i-1));
            }
            else {
                // Two situations:
                // (1) dp[i][j-2] is true, and there is 0 preceding element of '*';
                // (2) The last character of s should match the preceding element of '*';
                //     And, dp[i-1][j] should be true;
                dp[i][j] = (j>1 && dp[i][j-2]) ||
                           (i>0 && dp[i-1][j] && (p.charAt(j-2)=='.' || p.charAt(j-2)==s.charAt(i-1)));
            }
        }
    }

    return dp[sL][pL];
}
'''
class Solution:

	def isMatch(self, inString, regEx):
		# self.matchDict=dict()
		i=1
		while i<len(regEx)-2:
			if regEx[i]=='*':
				start=i-1
				end=start+2
				probe=start+4
				while regEx[probe-4: probe-2]==regEx[probe-2: probe]:
					end=probe
					probe+=2
				regEx=regEx[:start+2]+regEx[end:]
				i=start+1
			i=i+1

		# print regEx

		self.regEx=regEx

		return self.match(inString, regEx)



	def match(self, inString, regEx, i=0):
		# print inString, regEx, i

		if regEx==inString:
			return True

		if not regEx:
			return False

		if i<len(self.regEx)-1 and self.regEx[i+1]=='*':
			return self.match(inString, regEx[1:], i=i+1)

		if regEx[0] not in ['*', '.']:


			if not inString or inString[0]!=regEx[0]:
				return False
			else:
				return self.match(inString[1:], regEx[1:], i=i+1)

		elif regEx[0]=='.':
			return (len(inString)>0 and self.match(inString[1:], regEx[1:], i=i+1))
		else:

			if self.match(inString, regEx[1:], i=i+1):
				return True
			j=0
			while j < len(inString) and (self.regEx[i-1]=='.' or inString[j]==self.regEx[i-1]):
				if self.match(inString[j+1:], regEx[1:], i=i+1):
					return True
				j+=1

			return False



# this is too slow
	def isMatchOld(self, inString, regEx):
		counter=0
		lastCh=None
		for c in regEx:
			if c=='.':
				if len(inString)>counter:
					lastCh='.'
					counter=counter+1
				else:
					return (False)

			elif c=='*':
				if len(regEx)>counter+1:
				#	if len(inString)>counter:
						i=-1
						while (len(inString)>counter+i>=0):
							if(self.isMatch(inString[counter+i:],regEx[counter+1:])):
								return (True)
							elif((inString[counter+i]==lastCh) or lastCh=='.'):
								i=i+1
							else:return(False)
					# else:
					 	return (False)
				else:
					if len(inString)>counter:
						if lastCh=='.':
							return (True)
						for ch in inString[counter:]:
							if (ch != lastCh):
								return (False)
						return (True)
					else:
						return (True)
				counter=counter+1

			else:
				if len(inString)>counter:
					lastCh=regEx[counter]
					if (inString[counter]==lastCh):
						counter=counter+1
					else:
						if (len(regEx)>counter+2) and regEx[counter+1]=='*':
							return(self.isMatch(inString[counter:],regEx[counter+2:]))
						return (False)
				else:
					return ((len(regEx)==counter+2) and regEx[counter+1]=='*')

		return (len(inString)<=counter)

if __name__=="__main__":
	solution=Solution()
	print(solution.isMatch("a", ".*..a*"))
	print(solution.isMatch("HHelloooooop", "H*ello*"))
	print(solution.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
	print(solution.isMatch("ab", ".*"))
	print(solution.isMatch("aab", "c*a*b"))