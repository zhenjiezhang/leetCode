'''
140. Word Break II
Total Accepted: 48988 Total Submissions: 259194 Difficulty: Hard

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"]. 
'''


'''
This is not optimized, optimize it!
'''

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def tracing(self,s,starts):

        end=len(s)

        if end not in starts:
            return []

        sentences=[]
        for length in starts[end]:
            if length==end:
                sentences.append(s)
            else:
                lastSentences=self.tracing(s[:end-length],starts)
                for sentence in lastSentences:
                    sentences.append(sentence+" "+s[end-length:end])
        return sentences



    def wordBreak(self, s, dict):
        if s=="" and "" in dict:
            return [""]

        starts={0:[]}

        wordLen=set()
        for word in dict:
            wordLen.add(len(word))
        wordLen=list(wordLen)

        for i in range(len(s)):
            for length in wordLen:
                if i-length+1 in starts and s[i-length+1:i+1] in dict:
                    if i+1 in starts:
                        starts[i+1].append(length)
                    else:
                        starts[i+1]=[length]

        return self.tracing(s,starts)
        # print starts


if __name__=="__main__":
    solution=Solution()
    print solution.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
    print solution.wordBreak("", ["cat", "cats", "and", "sand", "dog"])
    print solution.wordBreak("a", [])
    print solution.wordBreak("aaaaaaa", ["aaaa","aa"])





