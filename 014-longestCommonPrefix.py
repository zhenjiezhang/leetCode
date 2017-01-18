'''
14. Longest Common Prefix
Total Accepted: 80169 Total Submissions: 298711 Difficulty: Easy

Write a function to find the longest common prefix string amongst an array of strings. 
'''


class Solution:
    # slightly faster, but easier to write:
    def longestCommonPrefix(self, strs):
        prefixLetters=zip(*strs)
        i=0
        while i <len(prefixLetters):
            if len(set(prefixLetters[i]))>1:
                break
            i+=1
        return strs[0][:i] if strs else ''




    #my old solution:
    def longestCommonPrefix_Straghtforward(self, strs):
    	prefix=''
    	if not strs:
    		return prefix
    	if len(strs)==1:
    		return strs[0]

        shortestLength=float('inf')
        for str in strs:
        	if len(str)<shortestLength:
        		shortestLength=len(str)

        for i in xrange(shortestLength):
        	c=strs[0][i]
        	for str in strs[1:]:
        		if str[i]!=c:
        			return prefix
        	prefix+=c

        return prefix

if __name__ == '__main__':
	strs=[
	'ggaa',
	'ggahhhgff',
	'ggaaaafa',
	'gggggga',
	'ggggggdfff'

	]
	solution=Solution()
	print solution.longestCommonPrefix(strs)




