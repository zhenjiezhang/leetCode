'''
115. Distinct Subsequences
Total Accepted: 45533 Total Submissions: 162868 Difficulty: Hard

Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3. 
'''


# better than mine: same speed but different strategy, more concise


'''
I independently came up with identical solution on 2nd round
'''

# /**
#  * Solution (DP):
#  * We keep a m*n matrix and scanning through string S, while
#  * m = T.length() + 1 and n = S.length() + 1
#  * and each cell in matrix Path[i][j] means the number of distinct subsequences of 
#  * T.substr(1...i) in S(1...j)
#  * 
#  * Path[i][j] = Path[i][j-1]            (discard S[j])
#  *              +     Path[i-1][j-1]    (S[j] == T[i] and we are going to use S[j])
#  *                 or 0                 (S[j] != T[i] so we could not use S[j])
#  * while Path[0][j] = 1 and Path[i][0] = 0.
#  */
# int numDistinct(string S, string T) {
#     int m = T.length();
#     int n = S.length();
#     if (m > n) return 0;    // impossible for subsequence
#     vector<vector<int>> path(m+1, vector<int>(n+1, 0));
#     for (int k = 0; k <= n; k++) path[0][k] = 1;    // initialization

#     for (int j = 1; j <= n; j++) {
#         for (int i = 1; i <= m; i++) {
#             path[i][j] = path[i][j-1] + (T[i-1] == S[j-1] ? path[i-1][j-1] : 0);
#         }
#     }

#     return path[m][n];
# }


class Solution:
    # @return an integer
    # this is slower, but in essence same to the preceeding algorithm.

    def numDistinct(self, S, T):

        if T=="":
            return 1
        if S=="":
            return 0

        TdistSet=set(T)
        TDict=dict()
        matchTable=[dict() for i in range(len(T))]

        for i in range(len(S)):
            if S[i] in TdistSet:
                if S[i]in TDict:
                    TDict[S[i]].append(i)
                else:
                    TDict[S[i]]=[i]

        if len(TDict)!=len(TdistSet):
            return 0
        
        for i in TDict[T[0]]:
            matchTable[0][i]=1

        i=0
        while i < len(T)-1:

            c=T[i+1]
            for posC in TDict[c]:

                matchTable[i+1][posC]=0
                for posI in TDict[T[i]]:
                    if posI < posC:
                        matchTable[i+1][posC]+=matchTable[i][posI]
            i+=1

        count=0

        for posC in matchTable[len(T)-1]:
            count+=matchTable[len(T)-1][posC]      

        return count

if __name__=="__main__":
    solution=Solution()
    print solution.numDistinct("","")
    print solution.numDistinct("","a")
    print solution.numDistinct("ababab","abb")
    print solution.numDistinct("b","a")





