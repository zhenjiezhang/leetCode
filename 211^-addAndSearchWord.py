'''
211. Add and Search Word - Data structure design
Total Accepted: 18683 Total Submissions: 91688 Difficulty: Medium

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.

click to show hint.
You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first. 
'''
class WordDictionary(object):

    class alphabetNode(object):
        def __init__(self):
            self.children=dict()
            self.wordEnd=False

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root=self.alphabetNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        r=self.root
        for w in word:
            if w not in r.children:
                r.children[w]=self.alphabetNode()

            r=r.children[w]

        r.wordEnd=True        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchPartial(word,self.root)

    def searchPartial(self, word, node):
        r=node
        for i in xrange(len(word)):
            if word[i]=='.':
                for subNode in r.children.values():
                    if self.searchPartial(word[i+1:],subNode):
                        return True
                return False
            elif word[i] not in r.children:
                return False
            else:
                r=r.children[word[i]]

        return r.wordEnd


        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
if __name__ == '__main__':
    wd=WordDictionary()
    wd.addWord("add")
    wd.addWord("cdb")
    # print wd.root.children.keys()
    print wd.search("c..")

