'''
131. Palindrome Partitioning
Total Accepted: 56721 Total Submissions: 207180 Difficulty: Medium

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
'''
class Solution:
    # @param s, a string
    # @return a list of lists of string

    def __init__(self):
        self.buf=dict()
        self.partialResults=dict()


    def isPalindrome(self,s):
        if s in self.buf:
            return self.buf[s]
        if s!=s[::-1]:
            self.buf[s]=False
            return False
        self.buf[s]=True
        return True




    def partition(self, s):
        if s in self.partialResults:
            return self.partialResults[s]

        if len(s)==0:
            return [[]]
        if len(s)==1:
            return [[s]]

        i=1
        partitions=[]
        while len(s)>=i:
            if self.isPalindrome(s[len(s)-i:]):
                prePartions=self.partition(s[:len(s)-i])
                for partition in prePartions:
                    partitions.append(partition+[s[len(s)-i:]])
            
            i+=1
        self.partialResults[s]=partitions
        return partitions






if __name__=="__main__":
	solution=Solution()
	print solution.partition("caacb")
	print solution.partition("aa")
	print solution.partition("")
	print solution.partition("c")
	print solution.partition("ababababababababababababcbabababababababababababa")
