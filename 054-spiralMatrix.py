class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        
        if not matrix:
            return matrix
        n=len(matrix)
        m=len(matrix[0])
        spiralNum=(min(m,n)+1)/2

        result=[]
        for i in xrange(spiralNum):
            result.extend(matrix[i][i:m-i])
            result.extend([matrix[j][m-1-i] for j in xrange(i+1,n-i)])
            result.extend([] if (n<m and n%2==1 and i==n/2) else matrix[n-1-i][i:m-1-i][::-1])
            result.extend([] if (m<n and m%2==1 and i==m/2) else [matrix[j][i] for j in xrange(n-2-i,i,-1)])
        return result

if __name__=="__main__":
    solution=Solution()
    print solution.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])
    print solution.spiralOrder([
 [1,1,1,1],
 [2,2,2,2],
 [3,3,3,3],
 [4,4,4,4]
])
    print solution.spiralOrder([
 [2],
 [3]
])

    print solution.spiralOrder([
 [2,3,4,5,6,7],
 [15,16,17,18,19,8],
 [14,13,12,11,10,9]
])

    print solution.spiralOrder([
 [2,3,4],
 [11,12,5],
 [10,13,6],
 [9,8,7],
])

    print solution.spiralOrder([
 [7],
 [6],
 [9],
])