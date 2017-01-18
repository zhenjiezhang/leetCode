'''
320. Generalized Abbreviation
Total Accepted: 3186 Total Submissions: 8041 Difficulty: Medium

Write a function to generate the generalized abbreviations of a word.

Example:

Given word = "word", return the following list (order does not matter):

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

'''

import re
class Solution(object):

    def __init__(self):
        self.cache=[[]]

    
    # for every character, it could be abbreviated, or not.  Exhaust all positilities from the beginning
    def generateAbbreviations(self, word):
        self.word=word
        self.indexcache=[[] for _ in xrange(len(word))]
        return self.dfs()


    def dfs(self, key=0):
        if key==len(self.word):
            return ['']
        if self.indexcache[key]:
            return self.indexcache[key]

        post=self.dfs(key+1)
        abbr=[(re.findall('^\d+',a)[0] if a and a[0].isdigit() else '', a) for a in post]
        abbr=[str(int(a[0])+1)+a[1][len(a[0]):] if a[0] else ('1'+a[1]) for a in abbr   ]
        # [(str(int(re.findall('^\d+',a)[0])+1)+a[len(re.findall('^\d+',a)[0]):]) if a and a[0].isdigit() else ('1'+a)   for a in post]

        abbrNot=[self.word[key]+a for a in post]
        self.indexcache[key]= abbr+abbrNot
        return self.indexcache[key]



    def generateAbbreviationsOld(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        #taking care of the cache
        if len(word)+1>len(self.cache):
            self.cache=[[]for _ in xrange(len(word)+1)]
        if self.cache[len(word)]:
            return self.cache[len(word)]

        #core solution
        result=[word]
        #length of first abbr
        for k in xrange(1, len(word)+1):
            #length before the first abbr
            for p in xrange(len(word)-k+1):
                pre=word[:p]+str(k)+(word[p+k] if p+k <len(word) else '')
                result.extend([pre+s for s in self.generateAbbreviationsOld(word[p+k+1:])])

        # put in cache
        self.cache[len(word)]=result

        return result



if __name__ == '__main__':
    solution=Solution()
    print solution.generateAbbreviations('')
    print solution.generateAbbreviationsOld('')


    print solution.generateAbbreviations('word')
    print solution.generateAbbreviationsOld('word')

