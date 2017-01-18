'''
87. Scramble String
Total Accepted: 40946 Total Submissions: 159081 Difficulty: Hard

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t

To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t

We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a

We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1. 
'''



'''
DP method.  Does not use isSameSet checking.  Combine both trick?

class Solution {
public:
    bool isScramble(string s1, string s2) {
        int sSize = s1.size(), len, i, j, k;
        if(0==sSize) return true;
        if(1==sSize) return s1==s2;
        bool isS[sSize+1][sSize][sSize];

        for(i=0; i<sSize; ++i)
            for(j=0; j<sSize; ++j)
                isS[1][i][j] = s1[i] == s2[j];

        for(len=2; len <=sSize; ++len)
            for(i=0; i<=sSize-len; ++i)
                for(j=0; j<=sSize-len; ++j)
                {
                    isS[len][i][j] = false;
                        for(k=1; k<len && !isS[len][i][j]; ++k)
                        {
                            isS[len][i][j] = isS[len][i][j] || (isS[k][i][j] && isS[len-k][i+k][j+k]);
                            isS[len][i][j] = isS[len][i][j] || (isS[k][i+len-k][j] && isS[len-k][i][j+k]);
                        }
                }
        return isS[sSize][0][0];            

    }
}; 

'''

class Solution:
    # @return a boolean
    def isSameSet(self, s1,s2):

    	if len(s1)!=len(s2):
    		return False

    	sSet=[0]*128
    	for a in s1:
    		sSet[ord(a)]+=1

    	for a in s2:
            c=ord(a)
            if sSet[c]==0:return False
            sSet[c]-=1

    	return sum(sSet)==0


    def isScramble(self, s1, s2):
    	if s1==s2:
    		return True

    	if not self.isSameSet(s1,s2):
    		return False

    	for i in range(1, len(s1)):
    		if (self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:])) or (self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:len(s1)-i])):
    			return True

    	return False









if __name__=="__main__":
	solution=Solution()
	print solution.isSameSet("","fdddd")
	print solution.isScramble("abc", "bca")
	# print solution.isScramble("acb","bca")
	# print solution.isScramble("abbbcbaaccacaacc","acaaaccabcabcbcb")
	# print solution.isScramble("ABCDE","CAEBD")
