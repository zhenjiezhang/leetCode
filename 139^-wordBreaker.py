from collections import deque
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean

    # this way I think is easier to follow, and is also faster, >=99%
    def wordBreak(self, s, wordDict):
        # have to check this because the first 0 in startpos is not check for s terminal in the loop
        if s in wordDict:
            return True

        wordLen=sorted(set([len(ss) for ss in wordDict]))
        wordStartPos=deque([0])
        wordStartSet={0}    # this is critical for speed
        while wordStartPos:
            pos=wordStartPos.pop()
            for l in wordLen:
                if pos+l <= len(s):
                    if s[pos:pos+l] in wordDict:
                        
                        if pos+l in wordStartSet:
                            continue
                        if pos+l==len(s):
                            return True

                        wordStartPos.append(pos+l)
                        wordStartSet.add(pos+l)
                       
                        
                else:
                    break

        return False








    def wordBreakOld(self, s, dict):
        if s in dict:
            return True
        starts={0}
        wordLen=set()
        for word in dict:
            wordLen.add(len(word))
        wordLen=list(wordLen)


        for i in range(len(s)):
            for length in wordLen:
                if i-length+1 in starts and s[i-length+1:i+1] in dict:
                    if i==len(s)-1:
                        return True
                    else:
                        starts.add(i+1)
        return False

if __name__=="__main__":
    solutiion=Solution()
    print solutiion.wordBreak("jeetcode",["jeet","code"])
    print solutiion.wordBreak("",["jeet","code"])
    print solutiion.wordBreak("",["","code"])

    print solutiion.wordBreak("jeetcode",[])





