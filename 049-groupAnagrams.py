'''
49. Group Anagrams
Total Accepted: 60814 Total Submissions: 235126 Difficulty: Medium

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    For the return value, each inner list's elements must follow the lexicographic order.
    All inputs will be in lower-case.

'''

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def groupAnagrams(self, strs):
        sortedStrings=[''.join(sorted(string)) for string in strs]
        dictionary=dict()

        for i in xrange(len(strs)):
            if sortedStrings[i] in dictionary:
                dictionary[sortedStrings[i]].append(i)
            else:
                dictionary[sortedStrings[i]]=[i]


        return [sorted([strs[dictionary[i][j]] for j in xrange(len(dictionary[i]))]) for i in dictionary]

if __name__=="__main__":
    solution=Solution()
    print solution.groupAnagrams([""])

    print solution.groupAnagrams(["cat","act","dog","god","ui"])
    print solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])



