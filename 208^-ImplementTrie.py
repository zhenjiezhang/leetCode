'''
208. Implement Trie (Prefix Tree)
Total Accepted: 27419 Total Submissions: 109103 Difficulty: Medium

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z. 


'''

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children=[None]*26
        self.wordEnd=False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        self.wordEnd=False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        r=self.root
        for c in word:
            c=ord(c)-97
            if not r.children[c]:
                r.children[c]=TrieNode()

            r=r.children[c]
        r.wordEnd=True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self.startsWith(word) and self.wordEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        r=self.root
        for c in prefix:
            c=ord(c)-97

            if not r.children[c]:
                return False
            r=r.children[c]
        self.wordEnd=r.wordEnd
        return True

        
if __name__ == '__main__':
# Your Trie object will be instantiated and called as such:
    trie = Trie()
    trie.insert("ab")
    print trie.search("a")
    print trie.startsWith("a")