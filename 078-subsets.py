


class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        result=[[]]
        
        for i in xrange(len(S)):
            result.extend([r+[S[i]] for r in result])
        return result




    def subsetsOld(self, S):
        S=sorted(S)
        n=len(S)
        results=[[]]
        baseList=[[[S[j]] for j in xrange(i+1)] for i in xrange(n)]
        progList=[[] for i in xrange(n)]
        for element in xrange(1,n):
            results+=baseList[n-1]

            for i in xrange(element,n):
                progList[i]=progList[i-1]+[shortList+[S[i]] for shortList in baseList[i-1]]
            baseList=progList
            progList=[[] for i in xrange(n)]
        results+=baseList[n-1]


        return results



if __name__=="__main__":
    solution=Solution()
    print solution.subsets([1])
    print solution.subsets([1,2,3])
