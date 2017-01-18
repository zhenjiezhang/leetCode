'''
79. Word Search
Total Accepted: 61784 Total Submissions: 282613 Difficulty: Medium

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

#could writ it simpler!

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean

    

    def findPath(self, index, i,j):
        if index==len(self.word):
            return True

        if i>0 and not self.pathMap[i-1][j] and self.board[i-1][j]==self.word[index]:
            self.pathMap[i-1][j]=1
            if self.findPath(index+1,i-1,j):
                return True
            else:
                self.pathMap[i-1][j]=0

        if j<len(self.board[0])-1 and not self.pathMap[i][j+1] and self.board[i][j+1]==self.word[index]:
            self.pathMap[i][j+1]=1
            if self.findPath(index+1,i,j+1):
                return True
            else:
                self.pathMap[i][j+1]=0

        if i<len(self.board)-1 and not self.pathMap[i+1][j] and self.board[i+1][j]==self.word[index]:
            self.pathMap[i+1][j]=1
            if self.findPath(index+1, i+1,j):
                return True
            else:
                self.pathMap[i+1][j]=0

        if j>0 and not self.pathMap[i][j-1] and self.board[i][j-1]==self.word[index]:
            self.pathMap[i][j-1]=1
            if self.findPath(index+1,i, j-1):
                return True
            else:
                self.pathMap[i][j-1]=0
        return False


    def exist(self, board, word):
        self.pathMap=[[0]*len(board[0]) for _ in xrange(len(board))]
        self.word=word
        self.board=board

        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                # print len(board[i])
                # print board[i][j]
                if board[i][j]==word[0]:
                    # print i,j
                    
                    self.pathMap[i][j]=1
                    if self.findPath(1,i,j):
                        return True
                    else:
                        self.pathMap[i][j]=0
        return False

if __name__=="__main__":
    solution=Solution()
    print solution.exist([
  "ABCE",
  "SFCS",
  "ADEE"
],"ABCCED")

print solution.exist(["ab","cd"], "acdb")
