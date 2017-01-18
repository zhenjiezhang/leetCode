


class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def pointRotate(self,matrix, x,y):
    	edge=len(matrix)-1
    	labels=[[x,y],[edge-y,x],[edge-x,edge-y],[y,edge-x]]

    	tmp=matrix[x][y]

    	for i in xrange(3):
    		matrix[labels[i][0]][labels[i][1]]=matrix[labels[i+1][0]][labels[i+1][1]]
    		# print labels[i][0],labels[i][1]
    	matrix[labels[3][0]][labels[3][1]]=tmp
    	# print labels[3][0],labels[3][1]



    def rotate(self, matrix):
        for i in xrange(len(matrix)/2):
        	for j in xrange(i,len(matrix)-1-i):
        		self.pointRotate(matrix,i,j)
        print matrix

if __name__=="__main__":

	matrix1=[[1,2,3],
			[4,5,6],
			[7,8,9]]

	matrix2=[[1,1,1,1],
			[2,2,2,2],
			[3,3,3,3],
			[4,4,4,4]]

	matrix3=[[1,2],
			[3,4],]



	solution=Solution()
	solution.rotate(matrix1)
	solution.rotate(matrix2)
	solution.rotate(matrix3)


