class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        letterList=[0]*26
        for i in xrange(len(s)):
            letterList[ord(s[i])-97]+=1
            letterList[ord(t[i])-97]-=1
        return not [l for l in letterList if l]



    def isAnagramoLD(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """


        '''
        this is slow due to join and sort
        could make a faster multiple line script
        '''
        return ''.join(sorted([c for c in s]))==''.join(sorted([c for c in t]))

if __name__=='__main__':
    print Solution().isAnagram('abbc','cba')
    print Solution().isAnagram('abbc','cbab')
