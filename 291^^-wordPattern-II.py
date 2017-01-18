'''
291. Word Pattern II
Total Accepted: 3199 Total Submissions: 9626 Difficulty: Hard

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Examples:

    pattern = "abab", str = "redblueredblue" should return true.
    pattern = "aaaa", str = "asdasdasdasd" should return true.
    pattern = "aabb", str = "xyzabcxzyabc" should return false.

I have no idea why this fucking code is way faster than mine.  Does using global variables slow things down?


def wordPatternMatch(self, pattern, str):
    return self.dfs(pattern, str, {})

def dfs(self, pattern, str, dict):
    if len(pattern) == 0 and len(str) > 0:
        return False
    if len(pattern) == len(str) == 0:
        return True
    for end in range(1, len(str)-len(pattern)+2): # +2 because it is the "end of an end"
        if pattern[0] not in dict and str[:end] not in dict.values():
            dict[pattern[0]] = str[:end]
            if self.dfs(pattern[1:], str[end:], dict):
                return True
            del dict[pattern[0]]
        elif pattern[0] in dict and dict[pattern[0]] == str[:end]:
            if self.dfs(pattern[1:], str[end:], dict):
                return True
    return False
'''

class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        self.patternDict={}
        self.wordToPattern=set()
        self.str=str
        self.pattern=pattern

        return self.findNext(0,0)

    def findNext(self, pp, ps):
        # print self.patternDict
        if pp>=len(self.pattern) and ps>=len(self.str):
            return True
        elif pp>=len(self.pattern) or ps>=len(self.str):
            return False

        if self.pattern[pp] not in self.patternDict:
            for wordLength in xrange(1,len(self.str)-ps-(len(self.pattern)-pp-1)+1):# it is very important to stop early, instead of going all the way to the string end. huge improve in speed

                if self.str[ps:ps+wordLength] in self.wordToPattern:
                    continue
                self.patternDict[self.pattern[pp]]=self.str[ps:ps+wordLength]
                self.wordToPattern.add(self.str[ps:ps+wordLength])

                if self.findNext(pp+1, ps+wordLength):
                    return True
                self.wordToPattern.remove(self.str[ps:ps+wordLength])

            self.patternDict.pop(self.pattern[pp],None)
            return False

        else:
            word=self.patternDict[self.pattern[pp]]
            if word==self.str[ps:ps+len(word)]:
                return self.findNext(pp+1, ps+len(word))
            else:
                return False

if __name__ == '__main__':
    solution=Solution()
    print solution.wordPatternMatch("abab", "redblueredblue")
    print solution.wordPatternMatch("aaaa", "asdasdasdasd")
    print solution.wordPatternMatch("aabb", "xyzabcxzyabc")
    print solution.wordPatternMatch("ab", "aa")
    print solution.wordPatternMatch("abba","dogcatcatdog")

    






