'''
91. Decode Ways
Total Accepted: 58342 Total Submissions: 344604 Difficulty: Medium

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2. 
'''
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        s+='0'
        ways=[1]*(len(s)+1)
        # ways.append[0]
        for i in xrange(len(s)-2, -1, -1):
            if s[i] not in ['1','2']:
                if s[i]=='0' and (i==0 or s[i-1] not in ['1','2']):
                    return 0
                elif s[i]=='0':
                    ways[i]=0
                    continue

                ways[i]=ways[i+1]
            elif s[i]=='1':
                ways[i]=ways[i+2] if s[i+1]=='0' else  ways[i+1]+ ways[i+2]
            else:
                ways[i]=ways[i+2] if s[i+1]=='0' else (ways[i+1]+ ways[i+2] if s[i+1] in '123456' else ways[i+1])
        
        return ways[0] if len(s)-1 else 0







    def numDecodingsOld(self, s):
        n=len(s)

        if n==0:
            return 0

        if s[0]=='0':
            return 0
        
        decodeWaysList=[0 for i in xrange(n)]
        decodeWaysList[0]=1
        if (n>=2 and s[1]=='0'):
            if s[0]=='1' or s[0]=='2':
                decodeWaysList[1]=1
            else:
                return 0
        elif n>=2:
            decodeWaysList[1]=2 if int(s[:2]) <=26 else 1

        if n<=2:
            return decodeWaysList[n-1]

        for i in xrange(2,n):
            if s[i]=='0':
                if s[i-1]=='1' or s[i-1]=='2':
                    decodeWaysList[i]+=decodeWaysList[i-2]
                else:
                    return 0
            else:

                decodeWaysList[i]=decodeWaysList[i-1]+(decodeWaysList[i-2] if (int(s[i-1:i+1])<=26 and s[i-1]!='0') else 0)

        return decodeWaysList[-1]

if __name__ == '__main__':
    solution=Solution()
    # print solution.numDecodings("12")
    print solution.numDecodings("110")
    print solution.numDecodings("100")
    print solution.numDecodings("9")



    print solution.numDecodings("12")

    print solution.numDecodings("101")
    print solution.numDecodingsOld("101")

