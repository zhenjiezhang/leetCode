'''
245. Shortest Word Distance III
Total Accepted: 5080 Total Submissions: 11150 Difficulty: Medium

This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list. 


'''
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        if word1==word2:
            idx=[i for i in xrange(len(words)) if words[i]==word1]
            return min([h-l for h,l in zip(idx[1:], idx)])

        lastIdx=-1
        minDist=len(words)

        for i in xrange(len(words)):
            if words[i]==word1 or words[i]==word2:
                if lastIdx>=0 and words[i]!=words[lastIdx]:
                    minDist=min(minDist, i-lastIdx)
                lastIdx=i
        return minDist
        

if __name__ == '__main__':
    s=Solution()
    print s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'practice')
    print s.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'makes')

