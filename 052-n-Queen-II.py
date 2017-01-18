class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count=0
        self.xySums=set()
        self.xyDifs=set()
        # self.x=set()
        self.y=dict()
        self.dfs(n)
        return self.count

    def dfs(self, n, x=0):

        if x==n:
            self.count+=1
            return

        for y in xrange(n):
            sumxy=x+y
            difxy=x-y
            if y in self.y or sumxy in self.xySums or difxy in self.xyDifs:
                continue
            else:
                self.y[y]=x
                self.xySums.add(sumxy)
                self.xyDifs.add(difxy)

                self.dfs(n,x=x+1)

                self.y.pop(y,0)
                self.xySums.remove(sumxy)
                self.xyDifs.remove(x-y)

if __name__ == '__main__':
    s=Solution()
    for i in xrange(9):
        print s.totalNQueens(i)
