import bisect

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers



    
    def combinationSum2(self, candidates, target, sort=True):
        if sort:
            candidates=sorted(candidates)

        candidates=candidates[:bisect.bisect(candidates, target)]
        limit=bisect.bisect(candidates, target/2)
        
        results=[[target]] if candidates and candidates[-1]==target else []

        i=0
        while i < limit and candidates[i]<target:
            j=bisect.bisect(candidates[:limit],candidates[i])

            for k in xrange(1,j-i+1):
                if candidates[i]*k>target:
                    i=j
                    break
                else:
                    iSegment=[candidates[i]]*k
                    if candidates[i]*k==target:
                        results+=[iSegment]
                        i=j
                        break
                    else:
                        results+=([iSegment+l for l in self.combinationSum2(candidates[j:], target-candidates[i]*k, sort=False)])
            i=j


        return results





    def combinationSum2Old(self, candidates, target):
        if not candidates:
            return []

        candidates=sorted(candidates)
        index=bisect.bisect(candidates, target)
        if index==0:
            return []
        

        results=[]

        
        preResults=self.combinationSum2(candidates[:index-1],target-candidates[index-1]) 
        for result in preResults:
            result+=[candidates[index-1]]
        results+=preResults

        results+=self.combinationSum2(candidates[:index-1],target)

        if target==candidates[index-1]:
            results.append([candidates[index-1]])


        return [list(i) for i in set([tuple(result) for result in results])]


            



if __name__=="__main__":
    solution=Solution()
    print solution.combinationSum2([1,2,3,5,2],5)