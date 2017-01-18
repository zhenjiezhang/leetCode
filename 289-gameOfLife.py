'''
289. Game of Life
Total Accepted: 12390 Total Submissions: 37156 Difficulty: Medium

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.

Follow up:

    Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?


'''
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                board[i][j]*=10


        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                xs=[i-1,i,i+1]
                ys=[j-1,j,j+1]
                for x in xs:    
                    for y in ys:
                        if x>=0 and x<len(board) and y>=0 and y<len(board[0]):
                            board[i][j]+=board[x][y]/10
                board[i][j]-=board[i][j]/10

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                a=board[i][j]/10
                b=board[i][j]-a*10
                if b<2 or b>3:
                    board[i][j]=0
                elif b==2:
                    board[i][j]=a
                else:
                    board[i][j]=1

if __name__=='__main__':
    a=[[0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,0],
            [0,0,1,0,0],
            [0,0,0,0,0]]
    # a=[[0]]
    Solution().gameOfLife(a)

    print a


