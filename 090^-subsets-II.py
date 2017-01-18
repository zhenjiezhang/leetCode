'''
90. Subsets II
Total Accepted: 57292 Total Submissions: 195533 Difficulty: Medium

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:

    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''


from collections import Counter
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        cnt=Counter(S)
        S=sorted(set(S))
        result=[[]]

        for s in S:
            result.extend([r+[s]*i for r in result for i in xrange(1,cnt[s]+1)])
        return result





    def subsetsWithDupOld(self, S):
        Selements=sorted(set(S))
        Smap={i:S.count(i) for i in Selements}
        numBefore=[int(sum([Smap[Selements[i]] for i in xrange(x)])) for x in xrange(len(Selements))]
        numBefore+=[len(S)]


        start=[[[] for i in xrange(len(Selements)+1)] for j in xrange(len(S)+1)]

        for j in xrange(1,len(Selements)+1):
            start[1][j]=[[Selements[i]]  for i in xrange(j)]
        for i in xrange(2,len(S)+1):
            begin=1

            while begin<len(Selements)+1 and numBefore[begin]<i:
                begin+=1
            
            for j in xrange(begin,len(Selements)+1):

                start[i][j]=[]

                for NumOfCurrentElement in xrange(max(0,i-numBefore[j-1]), min(i,Smap[Selements[j-1]])+1):

                    start[i][j]+=[lst+[Selements[j-1]]*(NumOfCurrentElement) for lst in start[i-NumOfCurrentElement][j-1]] if start[i-NumOfCurrentElement][j-1] else [[Selements[j-1]]*(NumOfCurrentElement)]

        return [i for a in [start[row][-1] for row in xrange(1,len(S)+1)] for i in a]+[[]]


if __name__ == '__main__':
    solution=Solution()
    print solution.subsetsWithDup([1,1,2,2,2])
    print solution.subsetsWithDupOld([1,1,2,2,2])





