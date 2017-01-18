'''
244. Shortest Word Distance II
Total Accepted: 5084 Total Submissions: 14590 Difficulty: Medium

This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list. 
'''

class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.wordsPositions=dict()
        for i in xrange(len(words)):
            if words[i] in self.wordsPositions:
                self.wordsPositions[words[i]].append(i)
            else:
                self.wordsPositions[words[i]]=[i]

    def shortest(self, word1, word2):
        list1, list2=self.wordsPositions[word1], self.wordsPositions[word2]
        p1=p2=0
        minDist=float('inf')
        while p1 <len(list1) and p2<len(list2):
            minDist=min(minDist, abs(list1[p1]-list2[p2]))
            if list1[p1]<list2[p2]: p1+=1
            else: p2+=1
        return minDist



        

    def shortestOld(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        list1, list2=self.wordsPositions[word1], self.wordsPositions[word2]
        p1=p2=0
        minDist=float('inf')

        while p1!=len(list1) and p2!=len(list2):
            
            if list1[p1]<list2[p2]:
                while p1!=len(list1) and list1[p1]<list2[p2]:
                    p1+=1
                if list2[p2]-list1[p1-1]< minDist:
                    minDist=list2[p2]-list1[p1-1]
            else:
                while p2!=len(list2) and list2[p2]<list1[p1]:
                    p2+=1
                if list1[p1]-list2[p2-1]< minDist:
                    minDist=list1[p1]-list2[p2-1]
        return minDist

if __name__ == '__main__':
    w=WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    print w.shortest('coding','practice')




        


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")