'''
290. Word Pattern
Total Accepted: 24878 Total Submissions: 89054 Difficulty: Easy

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:

    pattern = "abba", str = "dog cat cat dog" should return true.
    pattern = "abba", str = "dog cat cat fish" should return false.
    pattern = "aaaa", str = "dog cat cat dog" should return false.
    pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space. 
'''
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        mapping=dict()
        revMapping=dict()
        strTokens=str.split()
        if len(pattern)!=len(strTokens):
        	return False

        for p,t in zip(pattern,strTokens):
        	if p in mapping:
        		if t!=mapping[p]:
        			return False
        	if t in revMapping:
        		if p!=revMapping[t]:
        			return False
        	else:
        		mapping[p]=t
        		revMapping[t]=p



        return True

if __name__=='__main__':
	print Solution().wordPattern('abba',"dog dog dog dog")



        