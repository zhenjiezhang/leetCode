'''
311. Sparse Matrix Multiplication
Total Accepted: 3683 Total Submissions: 7867 Difficulty: Medium

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

                  '''

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        result=[[0]*len(B[0]) for _ in xrange(len(A))]

        #store indexes non-zero elements in each line of B.  Checking with any() first at this point speeds up from 124ms to 96ms
        Bi=[[i for i,v in enumerate(l) if v] if any(l) else [] for l in B]

        for i in xrange(len(A)):
            if not any(A[i]):
                continue
            for j in xrange(len(A[0])):
                if A[i][j]:
                    for k in Bi[j]:
                        result[i][k]+=A[i][j]*B[j][k]

        return result


    def multiplyOld(self
        , A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        result=[[0]*len(B[0]) for _ in xrange(len(A))]

        '''
        no need for the list.  you can check A on the fly and finish using it in one run like what 
        they do in GPU programming.
        '''
        # ANonzeros=[filter(lambda x: A[i][x]!=0, xrange(len(A[0]))) for i in xrange(len(A))]



        for i in xrange(len(A)):
            for j in xrange(len(A[0])):
                if A[i][j]:
                    for bCol in xrange(len(B[0])):
                        if B[j][bCol]:
                            result[i][bCol]+=A[i][j]*B[j][bCol]

        return result

if __name__ == '__main__':
    A=[
    [1,0,0],
    [-1,0,3]
    ]

    B=[
    [7,0,0],
    [0,0,0,],
    [0,0,1]
    ]

    solution=Solution()
    print solution.multiply([[1,-5]], [[12],[-1]])





