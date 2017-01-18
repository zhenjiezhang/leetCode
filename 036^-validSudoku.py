'''
36. Valid Sudoku
Total Accepted: 59843 Total Submissions: 205979 Difficulty: Easy

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated. 
'''


class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        checkSets=[[set()for i in xrange(9)],[set()for i in xrange(9)],[set()for i in xrange(9)]]
        for i in xrange(9):
            for j in xrange(9):
                a=board[i][j]
                if a=='.':
                    pass
                elif a in checkSets[0][i] or a in checkSets[1][j] or a in checkSets[2][i/3*3+j/3]:
                    return False
                else:
                    checkSets[0][i].add(a)
                    checkSets[1][j].add(a)
                    checkSets[2][i/3*3+j/3].add(a)

        return True



if __name__ == '__main__':
    solution=Solution()
    print solution.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
