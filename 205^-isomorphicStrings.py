'''
205. Isomorphic Strings
Total Accepted: 44144 Total Submissions: 156314 Difficulty: Easy

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.








def isIsomorphic(self, s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

'''
class Solution(object):
    def isIsomorphic(self, s, t):
        sMap=[-1]*128
        tMap=[-1]*128
        for i in xrange(len(s)):
            x,y=ord(s[i]), ord(t[i])
            if sMap[x]==-1 and tMap[y]==-1:
                sMap[x]=tMap[y]=i
            elif sMap[x]!=tMap[y]:
                return False
        return True






    def isIsomorphicOld(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        maps=dict()
        mapt=dict()

        n=len(s)

        for i in xrange(n):
            if s[i] not in maps and t[i] not in mapt:
                maps[s[i]]=mapt[t[i]]=i
            elif s[i] in maps and t[i] in mapt:
                if maps[s[i]]!=mapt[t[i]]:
                    return False
            else:
                return False
        return True
if __name__ == '__main__':
    print Solution().isIsomorphic("ooo", "bbr")
