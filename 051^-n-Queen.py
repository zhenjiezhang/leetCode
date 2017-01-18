class Solution:



    def solveNQueens(self, n):
        
        self.solutions=[]
        self.xySums=set()
        self.xyDifs=set()
        # self.x=set()
        self.y=dict()
        self.dfs(n)
        return self.solutions

    def dfs(self, n, x=0):

        if x==n:
            s=sorted([[self.y[y],y] for y in self.y])
            self.solutions.append(['.'*(y)+'Q'+'.'*(n-y-1) for _,y in s])
            return

        for y in xrange(n):
            
            if y in self.y or x+y in self.xySums or x-y in self.xyDifs:
                continue
            else:
                self.y[y]=x
                self.xySums.add(x+y)
                self.xyDifs.add(x-y)

                self.dfs(n,x=x+1)

                self.y.pop(y,0)
                self.xySums.remove(x+y)
                self.xyDifs.remove(x-y)










if __name__=="__main__":
    solution=Solution()
    for i in xrange(10):
        print solution.solveNQueens(i)




