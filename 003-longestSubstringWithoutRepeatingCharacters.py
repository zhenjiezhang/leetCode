'''
3. Longest Substring Without Repeating Characters
Total Accepted: 116413 Total Submissions: 552225 Difficulty: Medium

Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.
'''

'''
this is my old version, beats >90%:
class Solution:
	def lengthOfLongestSubstring (self, inString):
		chDict=dict()
		start=0
		maxLen=0
		cIdx=0
		for c in inString:
			if (c not in chDict) or (chDict[c] < start): # that's right, you do not need to pop ealier elements but then you do need to check each time
				chDict[c]=cIdx
			else:
				if ((cIdx-start)>maxLen):
					maxLen=(cIdx-start) 
				start=chDict[c]+1
				chDict[c]=cIdx

			cIdx=cIdx+1
		return max(maxLen,len(inString)-start)

'''
#my new version eliminating the use of a dict
#now beats 99%
class Solution:
	def lengthOfLongestSubstring (self, inString):
		chDict=[-1]*256
		start=0
		maxLen=0

		for i in xrange(len(inString)):
			asc=ord(inString[i])
			if chDict[asc]==-1 or chDict[asc]<start:
				chDict[asc]=i
			else:
				if maxLen<i-start:
					maxLen=i-start
				start=chDict[asc]+1
				chDict[asc]=i

		return max(maxLen, len(inString)-start)





if __name__=="__main__":
	solution=Solution()
	print (solution.lengthOfLongestSubstring ("qopubjguxhxdipfzwswybgfylqvjzhar"))
