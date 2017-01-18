'''
37. Sudoku Solver
Total Accepted: 43274 Total Submissions: 182779 Difficulty: Hard

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.


A sudoku puzzle...


...and its solution numbers marked in red. 
'''

'''
idea to save time:
pre-compute the allowed candidates for each '.' cell, based on the given board.  This is fast.  
during backtracking, maintained dynanmic additional sets to enbody additional constrains as tentative values are set.
This should make it faster, since not everything, but only those change will be checked each time.
'''
class Solution:

    def solveSudoku(self, board):
        result=[[-1 if board[i][j]=='.' else int(board[i][j]) for j in xrange(9)] for i in xrange(9)]
        self.solveSudokuRecurse(result)

        board[:]=[''.join([str(result[i][j]) if result[i][j]>0 else '.' for j in xrange(9)]) for i in xrange(9)][:]
    def solveSudokuRecurse(self, board, index=[0,0]):
        for i in xrange(index[0], 9):
            for j in xrange(index[1] if i==index[0] else 0, 9):
                if board[i][j]==-1:
                    candidates={i for i in xrange(1,10)}-{board[i][p] for p in xrange(9)}-\
                    {board[p][j] for p in xrange(9)}-{board[i-i%3+p/3][j-j%3+p%3] for p in xrange(9)}
                    if not candidates:
                        return False
                    else:
                        for c in candidates:
                            board[i][j]=c
                            if self.solveSudokuRecurse(board, index=[i,j]):
                                return True
                            else:
                                board[i][j]=-1
                        return False
        return True












# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# The old solver

# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    sudoku=[[0]*9 for i in range(9)]
    completeset=range (10)
    completeset.remove(0)
    completeset=set(completeset)

    rowElements, colElements=[set() for i in range(9)], [set() for i in range(9)]
    grdElements=[[set() for i in range(3)] for j in range (3)]
    missingElements=[dict() for i in range(9)]    # 9 lines, dict(column)=possible candidate elements

    elementRows=[set() for i in range (9)]    # for looking up whether a row contains a specitied element, to look up element 9, use "row in elementRows[8]""
    elementCols=[set() for i in range (9)]
    elementGrid=[set() for i in range (9)]    # stores tuples for index of grids (0:2,0:2)



    def initialization(self):

        self.rowElements, self.colElements=[set() for i in range(9)], [set() for i in range(9)]
        self.grdElements=[[set() for i in range(3)] for j in range (3)]
        self.missingElements=[dict() for i in range(9)]
        for i in range (9):
            for j in range (9):
                if self.sudoku[i][j]!='.':

                    self.deposit(self.sudoku[i][j], i, j)

                else:
                    self.missingElements[i][j]=[]    #initialize missing element indexes as i,j, and prepare the list for candidates

    def findCandidates(self):
        preProc=True
        while (preProc==True):
            preProc=False
            for i in range (9):
                for j in range(9):
                    if self.missingElements[i][j]!=None:
                        self.missingElements[i][j]=self.completeset-self.rowElements[i]-self.colElements[j]-self.grdElements[i/3][j/3]
                        if len(self.missingElements[i][j])==1:
                            number=iter(self.missingElements[i][j]).next()

                            self.deposit(number,i,j)

                            preProc=True

    def deposit (self, number, i, j):

        self.sudoku[i][j]=number

        self.rowElements[i].add(number)
        self.colElements[j].add(number)
        self.grdElements[i/3][j/3].add(number)

        self.elementRows[number-1].add(i)
        self.elementCols[number-1].add(j)
        self.elementGrid[number-1].add((i/3,j/3))
        self.missingElements[i][j]=None



    def findNumPos(self):
        research=True
        while research==True:
            research=False

            for row in range(9):
                if (self.completeset-self.rowElements[row]):
                    for col in range(9):
                        uniqSet=set([])
                        if self.missingElements[row][col]!=None:
                            uniqSet=self.missingElements[row][col]
                            for others in range(9):
                                if col!=others and self.missingElements[row][others]!=None:
                                    uniqSet=uniqSet-self.missingElements[row][others]
                        if uniqSet:
                            research=True
                            self.deposit(iter(uniqSet).next(),row, col)

            for col in range(9):
                if (self.completeset-self.colElements[col]):
                        
                    for row in range(9):
                        uniqSet=set([])

                        if self.missingElements[row][col]!=None:
                            uniqSet=self.missingElements[row][col]
                            for others in range(9):
                                if row!=others and self.missingElements[others][col]!=None:
                                    uniqSet=uniqSet-self.missingElements[others][col]
                        if uniqSet:
                            research=True
                            self.deposit(iter(uniqSet).next(),row, col)

            for i in range(3):
                for j in range(3):
                    if (self.completeset-self.grdElements[i][j]):
                        
                        for row in range(3):
                            row=i*3+row
                            for col in range(3):                            
                                col=j*3+col
                                uniqSet=set([])
                                if self.missingElements[row][col]!=None:
                                    uniqSet=self.missingElements[row][col]
                                    for otherRow in range(3):
                                        otherRow=otherRow+i*3
                                        for otherCol in range(3):
                                            otherCol=otherCol+j*3
                                            if ((row!=otherRow) or (col!=otherCol)) and (self.missingElements[otherRow][otherCol]!=None):
                                                uniqSet=uniqSet-self.missingElements[otherRow][otherCol]
                                if uniqSet:
                                    research=True
                                    self.deposit(iter(uniqSet).next(),row, col)

        tracingQueues=[]
        for i in range(9):
            for j in range(9):
                if self.missingElements[i][j]:
                    tracingQueues.append([(i,j), list(self.missingElements[i][j])])


        tracer=0
        goal=len(tracingQueues)
        while((0<=tracer<goal)):

            j=tracingQueues[tracer][0][1]
            queue=tracingQueues[tracer][1]
            

            if (self.sudoku[i][j]!='.'):
                self.sudoku[i][j]='.'
                self.rowElements[i].remove(number)
                self.colElements[j].remove(number)
                self.grdElements[i/3][j/3].remove(number)



            while(len(queue)>0):
                currentNum=queue.pop()
                if currentNum in (self.completeset-self.rowElements[i]-self.colElements[j]-self.grdElements[i/3][j/3]):
                    self.sudoku[i][j]=number
                    self.rowElements[i].add(number)
                    self.colElements[j].add(number)
                    self.grdElements[i/3][j/3].add(number)



                    tracer=tracer+1
                    break

                tracer=tracer-1
        if tracer<0: print tracer





    def solveSudokuOld(self, board):
        for i in range (9):
            for j in range (9):
                if board[i][j]=='.':
                    self.sudoku[i][j]='.'
                else:
                    self.sudoku[i][j]=int(board[i][j])


        self.initialization()

        self.findCandidates()

        self.popTracer()

        results=[''.join(map(str,self.sudoku[i])) for i in range(9)]

        for i in range(9):
            board[i]=results[i]


if __name__=="__main__":
    solution=Solution()
    # print (
    #     solution.solveSudoku(
    #     [[5,3,'.','.',7,'.','.','.','.'],
    #      [6,'.','.',1,9,5,'.','.','.'],
    #      ['.',9,8,'.','.','.','.',6,'.'],
    #      [8,'.','.','.',6,'.','.','.',3],
    #      [4,'.','.',8,'.',3,'.','.',1],
    #      [7,'.','.','.',2,'.','.','.',6],
    #      ['.',6,'.','.','.','.',2,8,'.'],
    #      ['.','.','.',4,1,9,'.','.',5],
    #      ['.','.','.','.',8,'.','.',7,9]])
    #     )
    input0=["...2...63","3....54.1","..1..398.",".......9.","...538...",".3.......",".263..5..","5.37....8","47...1..."]

    # input1 = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."] 

    # input2 = ["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
    
    solution.solveSudoku(input0)
    # solution.solveSudoku(input1)
    # solution.solveSudoku(input2)

    print input0
    # print input1
    # print input2
    
    # for i in range(9):
    #     for j in range(9):
    #         print result[i][j], #if result[i][j]!='.' else 0,
    #     print