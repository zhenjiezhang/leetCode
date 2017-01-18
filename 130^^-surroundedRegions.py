from collections import deque
class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    displacements = [[1, 0], [-1, 1], [-1, -1], [1, -1]]
# (i,j) -> (i+1,j) -> (i,j+1) -> (i-1,j) -> (i,j-1)

    def bfs(self, board, i, j, m, n):
        # O: White, X:Black, G:Gray
        dq = collections.deque([[i, j]])
        board[i][j] = 'G'
        while dq:
            i, j = dq.popleft()
            for di, dj in Solution.displacements:
                i += di
                j += dj
                if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                    dq.append([i, j])
                    board[i][j] = 'G'

    def solve(self, board):
        if len(board) < 3 or len(board[0]) < 3:
            return
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in 0, n - 1:
                if board[i][j] == 'O':
                    self.bfs(board, i, j, m, n)

        for i in 0, m - 1:
            for j in xrange(1, n - 1):
                if board[i][j] == 'O':
                    self.bfs(board, i, j, m, n)

        for row in board:
            for j in xrange(n):
                if row[j] != 'X':
                    row[j] = 'X' if row[j] == 'O' else 'O'



    def solve_mine(self, board):
        # converting string to lists first slows down significantly
        # myBoard=[[c for c in line] for line in board]
        for i, j in [[a,b] for a in xrange(len(board)) for b in xrange(len(board[0]))\
         if a in [0, len(board)-1] or b in [0, len(board[0])-1]]:
                if board[i][j]=='O':
                    board[i][j]='L'
                    buf=deque([[i,j]])
                    while buf:
                        bx,by=buf.popleft()
                        # could save this to displacements, and do not have to reconstruct for each step
                        neighbors=[[bx, by-1], [bx, by+1],[bx-1, by],[bx+1,by]]
                        for x,y in neighbors:
                            if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y]=='O':
                                buf.append([x,y])
                                board[x][y]='L'
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j]=='L':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
        # board[:]=[''.join(line) for line in myBoard]



    def solve_naive(self, board):
        myBoard=[[c for c in line] for line in board]

        for i in xrange(len(myBoard)):
            for j in xrange(len(myBoard[0])):
                if myBoard[i][j]=='O':
                    live=False
                    myBoard[i][j]='X'
                    front=[[i,j]]
                    thisPatch=[[i,j]]

                    while front: 
                        thisPatch.extend(front)
                        newFront=[]
                        for fx, fy in front:
                            neighbors=[[fx, fy-1], [fx, fy+1],[fx-1, fy],[fx+1,fy]]
                            for x,y in neighbors:
                                if 0<=x<len(myBoard) and 0<=y<len(myBoard[0]):
                                    if myBoard[x][y]=='O':
                                        newFront.append([x,y])
                                        thisPatch.append([x,y])
                                        myBoard[x][y]='X'
                                else:
                                    live=True
                        front=newFront
                    if live:
                        for livex, livey in thisPatch:
                            myBoard[livex][livey]='L'

        for i in xrange(len(myBoard)):
            for j in xrange(len(myBoard[0])):
                if myBoard[i][j]=='L':
                    myBoard[i][j]='O'
                

        board[:]=[''.join(line) for line in myBoard]


'''
old
'''

    # def merge(self, list1,list2):
    #     if list1[1]==1 or list2[1]==1:
    #         list1[1]=list2[1]=1

    #     if len(list1[0])<=len(list2[0]):
    #         l1=list1
    #         l2=list2
    #     else:
    #         l1=list2
    #         l2=list1
    #     l2[0]+=l1[0]
    #     for point in l1[0]:
    #         self.oDict[point]=l2

    # def solveOld(self, board):
    #     self.oDict=dict()
    #     self.groups=set()
    #     for i in xrange(len(board)):
    #         for j in xrange(len(board[0])):
    #             if board[i][j]=='O':
    #                 if i>0 and (i-1,j) in self.oDict:
    #                     self.oDict[(i-1,j)][0].append((i,j))
    #                     self.oDict[(i,j)]=self.oDict[(i-1,j)]

    #                 if j>0 and (i,j-1) in self.oDict:
    #                     if (i,j) in self.oDict and self.oDict[(i,j)] != self.oDict[(i,j-1)]:
    #                         self.merge(self.oDict[(i,j)],self.oDict[(i,j-1)])
    #                     elif (i,j) not in self.oDict:
    #                         self.oDict[(i,j-1)][0].append((i,j))
    #                         self.oDict[(i,j)]=self.oDict[(i,j-1)]
    #                 if (i,j) not in self.oDict:
    #                     self.oDict[(i,j)]=[[(i,j)],0]
    #                 if i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1:
    #                     self.oDict[(i,j)][1]=1

    #     for point in self.oDict:
    #         if self.oDict[point][1]==0:
    #             s=list(board[point[0]])
    #             s[point[1]]='X'
    #             board[point[0]]=''.join(s)


        



if __name__ == '__main__':
    solution=Solution()
    board=  ["XXX","XOX","XXX"]
    solution.solve(board)
    print board