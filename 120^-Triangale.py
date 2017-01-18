'''
120. Triangle
Total Accepted: 60078 Total Submissions: 206918 Difficulty: Medium

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11). 

'''


class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer


    # this is a one liner for fun :)  Node that this creates a new triangle [::-1] was used, so unfortunately space was not k. 
    def minimumTotal(self, triangle):

        return reduce(lambda x, y: [min(x[b], x[b+1])+y[b] for b in xrange(len(y))], triangle[::-1], [0]*(len(triangle)+1))[0]


    # this is my original expended version of that one liner, faster than that, achieved 44ms, but I guess the running time varies enough each time you submit, 
    # so that the real difference is not significant
    def minimumTotalExpended(self, triangle):

        triangle.append([0]*(len(triangle)+1))
        return reduce(lambda x, y: [min(x[b], x[b+1])+y[b] for b in xrange(len(y))], triangle[::-1])[0]


    # further expend, in this one, no extra triangle was created, only one line each time, so space is k.
    def minimumTotalDP(self, triangle):
        
        base=[0]*(len(triangle)+1)
        for i in xrange(len(triangle)-1, -1, -1):
            base=[min(base[b], base[b+1])+triangle[i][b] for b in xrange(i+1)]
        return base[0]



    #recursive, top down, slower.  I think this is not well written, could be imporved much.
    def minimumTotalRecurse(self, triangle):
        self.triangle=triangle
        self.cache=dict()
        return self.recurse(0,0) if triangle else 0

    def recurse(self, level, i):
        if (level,i) in self.cache:
            return self.cache[(level,i)]

        if level==len(self.triangle)-1:
            return self.triangle[level][i]

        res=self.triangle[level][i]+min(self.recurse(level+1, i), self.recurse(level+1, i+1))
        self.cache[(level, i)]=res

        return res


    # DP from top down, I wrote this one when I started learning programing.  Not a good piece for sure...speed was not bad though.
    def minimumTotalTopDownDP(self, triangle):
        minSum=float('inf')
        if not triangle:
            return 0
        level1Sum=[triangle[0][0]]
        level2Sum=[]
        while len(triangle)>len(level1Sum):
            level2Sum=[triangle[len(level1Sum)][i]+min((level1Sum[i] if i < len(level1Sum) else float('inf')),(level1Sum[i-1] if i>=1 else float('inf')) ) \
            for i in xrange(len(level1Sum)+1)]
            level1Sum=level2Sum
            level2Sum=[]

        return min(level1Sum)



if __name__ == '__main__':
    solution=Solution()
    print solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
    print solution.minimumTotalOld([[2],[3,4],[6,5,7],[4,1,8,3]])

    print solution.minimumTotal([])


