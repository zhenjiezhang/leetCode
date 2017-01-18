
'''
316. Remove Duplicate Letters
Total Accepted: 8134 Total Submissions: 34454 Difficulty: Medium

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:

Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb" 


my post:
https://leetcode.com/discuss/73932/python-no-recursion-o-n
'''
class Solution(object):
    def removeDuplicateLetters(self, s):

        indexes={}        
        for i in xrange(len(s)-1,-1,-1):
            if s[i] in indexes:
                indexes[s[i]].append(i)
            else:
                indexes[s[i]]=[i]

        cList=sorted(indexes.keys())
        result=''
        while len(result)<len(indexes):
            bottom=min([indexes[c][0] for c in cList])
            candidate=0
            while indexes[cList[candidate]][-1]>bottom:
                candidate+=1
            result+=cList[candidate]
            cList=cList[:candidate]+cList[candidate+1:]

            for c in cList:
                while indexes[c][-1]<indexes[result[-1]][-1]:
                    indexes[c].pop()
        return result


if __name__ == '__main__':
    from time import time
    for e in range(10, 18):
        n = 2**e
        s = 'a' * n
        t0 = time()
        Solution().removeDuplicateLetters(s)
        t = time() - t0
        print '%7.3f seconds for n = %d' % (t, n)

