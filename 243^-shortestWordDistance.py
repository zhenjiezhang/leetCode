'''
243. Shortest Word Distance
Total Accepted: 7289 Total Submissions: 15970 Difficulty: Easy

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list. 
'''
class Solution(object):


    def shortestDistance(self, words, word1, word2):
        lastIdx=-1
        minDist=len(words)

        for i in xrange(len(words)):
            if words[i]==word1 or words[i]==word2:
                if lastIdx>=0 and words[i]!=words[lastIdx]:
                    minDist=min(minDist, i-lastIdx)
                lastIdx=i
        return minDist





    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        wordPositions=[-float('inf'),-float('inf')]
        minDist=float('inf')
        for i in xrange(len(words)):
            if words[i]==word1:
                wordPositions[0]=i
                if i-wordPositions[1]<minDist:
                    minDist=i-wordPositions[1]
            elif words[i]==word2:
                wordPositions[1]=i
                if i-wordPositions[0]<minDist:
                    minDist=i-wordPositions[0]
        return minDist

if __name__ == '__main__':
    s=Solution()
    print s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'practice')
