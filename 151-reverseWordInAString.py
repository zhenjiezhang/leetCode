class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])



    def reverseWordsOld(self, s):
        wordStack=[]
        reverse=[]
        s+=' '
        for c in s:
        	if c!=' ':
        		wordStack.append(c)
        	else:
        		if not wordStack:
        			continue
        		reverse=[''.join(wordStack)]+reverse
        		wordStack=[]
        return ' '.join(reverse)

if __name__ == '__main__':
	solution=Solution()
	print solution.reverseWords("the  sky is blue")
	print solution.reverseWords('a')

