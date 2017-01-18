'''
132. Palindrome Partitioning II
Total Accepted: 44847 Total Submissions: 213236 Difficulty: Hard

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut. 
'''
'''
This is not faster, but simpler.  Same general thought.

public int minCut(String s) {
    char[] c = s.toCharArray();
    int n = c.length;
    int[] cut = new int[n];
    boolean[][] pal = new boolean[n][n];

    for(int i = 0; i < n; i++) {
        int min = i;
        for(int j = 0; j <= i; j++) {
            if(c[j] == c[i] && (j + 1 > i - 1 || pal[j + 1][i - 1])) {
                pal[j][i] = true;  
                min = j == 0 ? 0 : Math.min(min, cut[j - 1] + 1);
            }
        }
        cut[i] = min;
    }
    return cut[n - 1];
}
'''

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self,s):
        s=[c for c in s]

        # these lines are really not needed.  They only speed up special cases in OJ.
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        # map pal ending to a list of starts, inclusive
        # find out all pal starts corresponding to ending at i
        palEndingAtMap=[[i] for i in xrange(len(s))]
        for i in xrange(len(s)):
            for j in xrange(1,min(i+1, len(s)-i)):
                if s[i-j]==s[i+j]:
                    palEndingAtMap[i+j].append(i-j)
                else:
                    break
            for j in xrange(min(i+1, len(s)-i-1)):
                if s[i-j]==s[i+1+j]:
                    palEndingAtMap[i+1+j].append(i-j)
                else:
                    break

        # DP find minCuts
        mCutArray=[i for i in xrange(len(s))]
        for i in xrange(len(s)):

            for start in xrange(-1, -len(palEndingAtMap[i])-1, -1):
                if palEndingAtMap[i][start]==0:
                    mCutArray[i]=0
                    break
                if mCutArray[i]>mCutArray[palEndingAtMap[i][start]-1]+1:
                    mCutArray[i]=mCutArray[palEndingAtMap[i][start]-1]+1
        return mCutArray[-1]






    def minCutOld(self,s):
        # these lines are really not needed.  They only speed up special cases in OJ.
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        # list speeds up a little bit above string                
        s=[c for c in s]


        minCutArray=[i-1 for i in range(len(s)+1)]

        for i in range(len(s)):
            j=0
            while i>=j and i+j< len(s) and s[i+j]==s[i-j]:
                j+=1
                minCutArray[i+j]=min(minCutArray[i-j+1]+1,minCutArray[i+j])

            j=0
            while i>=j and i+j+1<len(s) and s[i-j]==s[i+j+1]:
                j+=1
                minCutArray[i+j+1]=min(minCutArray[i-j+1]+1,minCutArray[i+j+1])

        return minCutArray[-1]











        


if __name__=="__main__":

    solution=Solution()
    # print solution.minCut("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    # print solution.minCut("aabaaaccad")
    print solution.minCut("ccaacabacb")
    print solution.minCutOld("ccaacabacb")

    # print solution.minCut("fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi")

        