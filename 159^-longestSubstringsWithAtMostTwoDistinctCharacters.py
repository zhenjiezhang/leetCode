'''
159. Longest Substring with At Most Two Distinct Characters
Total Accepted: 8657 Total Submissions: 26215 Difficulty: Hard

Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s ="eceba",

T is "ece" which its length is 3. 


'''




# use two pointers should be faster

class Solution:
    # @param s, a string
    # @return an integer


    def lengthOfLongestSubstringTwoDistinct(self, s):
        # faster not to convert to a list
        # s=[c for c in s]
        if len(s)<=2:
            return len(s)
        maxLen=0


        windowSet=s[:1] if s[1]==s[0] else s[:2]
        lastPureStart=0 if s[1]==s[0] else 1
        curLen=2

        for i in xrange(2,len(s)):
            if s[i] in windowSet:
                curLen+=1
                if s[i]!=s[i-1]:
                    lastPureStart=i
            elif len(windowSet)==1:
                windowSet+=s[i]
                curLen+=1
                lastPureStart=i
            else:
                if maxLen<curLen:
                    maxLen=curLen

                curLen=i-lastPureStart+1
                windowSet=s[i-1:i+1]
                lastPureStart=i
        return max(maxLen, curLen)









    def lengthOfLongestSubstringTwoDistinctOld(self, s):
        last=None
        lastLength=0
        lastTwo=set()
        lastTwoLength=0

        maxLength=0
        maxTwo=set()
        curCount=0


        if not s:
        	return 0

        if len(s)<3:
            return len(s)


        lastTwo=set(s[:2])

        i=2
        while i<len(s) and len(lastTwo)<2:
            lastTwo.add(s[i])
            i+=1


        last=s[i-1]
        
        lastLength+=1

        while i < len(s) and s[i] in lastTwo:
            i+=1

        lastTwoLength=i
        last=s[i-1]

        j=i-1


        while j>=0 and s[j]==last:
            j-=1

        lastLength=i-j-1
        maxLength=lastTwoLength
        maxTwo=set(list(lastTwo))


        while i < len(s):

            if s[i] in lastTwo:
                lastTwoLength+=1
                if s[i]==last:
                    lastLength+=1
                else:
                	last=s[i]
                	lastLength=1

            else:
                lastTwoLength=lastLength+1
                lastTwo=set()
                lastTwo.add(last)
                lastTwo.add(s[i])
                lastLength=1
                last=s[i]
            if lastTwoLength > maxLength:
                    maxLength=lastTwoLength
                    maxTwo=set(list(lastTwo))

            i+=1

        return maxLength

if __name__=="__main__":
    solution=Solution()
    print solution.lengthOfLongestSubstringTwoDistinct("aac")

    print solution.lengthOfLongestSubstringTwoDistinct("tttyyyyyyyiiii")
    print solution.lengthOfLongestSubstringTwoDistinctOld("tttyyyyyyyiiii")

    print solution.lengthOfLongestSubstringTwoDistinct("abccbbcccaaacaca")
    print solution.lengthOfLongestSubstringTwoDistinctOld("abccbbcccaaacaca")



