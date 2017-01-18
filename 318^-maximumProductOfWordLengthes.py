'''
318. Maximum Product of Word Lengths
Total Accepted: 11596 Total Submissions: 29873 Difficulty: Medium

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:

Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:

Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words. 
'''

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """


        binaryWords={}
        for w in words:
            if not w:
                continue

            b=reduce(lambda x,y:x|y, [1<<(ord(c)-ord('a')) for c in w])
            if b in binaryWords and  len(w)<=binaryWords[b]:
                continue
            else:
                binaryWords[b]=len(w)

        allPossibilities=[binaryWords[b1]*binaryWords[b2] for b1 in binaryWords.keys() for b2 \
            in binaryWords.keys() if not b1&b2]
        return max(allPossibilities) if allPossibilities else 0


if __name__ == '__main__':
    print Solution().maxProduct([''])