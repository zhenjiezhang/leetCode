'''
302. Smallest Rectangle Enclosing Black Pixels
Total Accepted: 3201 Total Submissions: 8449 Difficulty: Hard

An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

For example, given the following image:

[
  "0010",
  "0110",
  "0100"
]

and x = 0, y = 2,

Return 6. 


my solution is pretty slow, but still got accepted. 

Binary search would have been faster:
Suppose we have a 2D array

"000000111000000"
"000000101000000"
"000000101100000"
"000001100100000"

Imagine we project the 2D array to the bottom axis with the rule "if a column has any black pixel it's projection is black otherwise white". The projected 1D array is

"000001111100000"

    Theorem

    If there are only one black pixel region, then in a projected 1D array all the black pixels are connected.

    Proof by contradiction

    Assume to the contrary that there are disconnected black pixels at i and j where i < j in the 1D projection array. Thus there exists one column k, k in (i, j) and and the column k in the 2D array has no black pixel. Therefore in the 2D array there exists at least 2 black pixel regions separated by column k which contradicting the condition of "only one black pixel region".

    Therefore we conclude that all the black pixels in the 1D projection array is connected.

This means we can do a binary search in each half to find the boundaries, if we know one black pixel's position. And we do know that.

To find the left boundary, do the binary search in the [0, y) range and find the first column vector who has any black pixel.

To determine if a column vector has a black pixel is O(m) so the search in total is O(m log n)

We can do the same for the other boundaries. The area is then calculated by the boundaries. Thus the algorithm runs in O(m log n + n log m)

'''


'''

Alternative, O(mn)
def minArea(self, image, x, y):
    a, b = (sum('1' in row for row in image)
            for image in (image, zip(*image)))
    return a * b

Or:

def minArea(self, image, x, y):
    return sum('1' in r for r in image) * sum('1' in r for r in zip(*image))

'''


class Solution(object):
    def minArea(self, image, x, y):
        up=self.findEdge(image[:x+1])
        down=len(image)-self.findEdge(image[x:][::-1])-1
        rotated=zip(*image)

        left=self.findEdge(rotated[:y+1])
        right=len(image[0])-self.findEdge(rotated[y:][::-1])-1

        return (down-up+1)*(right-left+1)

    def findEdge(self, image):
        l,r=0,len(image)-1
        while l<=r:
            m=(l+r)/2
            if '1' in image[m] and (m==0 or '1' not in image[m-1]):
                return m
            elif '1' in image[m]:
                r=m-1
            else:
                l=m+1







    def minAreaExplore(self, image, x, y):
        self.image=[[c for c in l]  for l in image]
        self.left=x
        self.right=x
        self.top=y
        self.bottom=y

        self.dfs(x,y)
        return (self.right-self.left+1)*(self.bottom-self.top+1)

    def dfs(self, x,y):
        if x<self.left:
            self.left=x
        elif x>self.right:
            self.right=x

        if y<self.top:
            self.top=y
        elif y>self.bottom:
            self.bottom=y

        self.image[x][y]=-1
        if x>0 and self.image[x-1][y]=='1':
            self.dfs(x-1,y)
        if x<len(self.image)-1 and self.image[x+1][y]=='1':
            self.dfs(x+1,y)
        if y>0 and self.image[x][y-1]=='1':
            self.dfs(x,y-1)
        if y<len(self.image[0])-1 and self.image[x][y+1]=='1':
            self.dfs(x,y+1)




    def minAreaOld(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """

        # visited=[[[0]*4 for _ in xrange(len(image[0]))]for _ in xrange(len(image))]
        self.image=image
        self.visited=set()




        while x!=0 and image[x-1][y]=='1':
            x-=1

        if image[x][y]==0:
            x+=1

        self.left=self.right=x
        self.up=self.low=y

        self.walkEdge(x,y)
        return (self.right-self.left+1)*(self.low-self.up+1)
        

    def unvisitedNeighbors(self, x,y):
        probes=[]
        if x!=0 and self.image[x-1][y]=='1' and (x-1, y) not in self.visited:
            probes.append([x-1,y])
        if x!=len(self.image)-1 and self.image[x+1][y]=='1' and (x+1, y) not in self.visited:
            probes.append([x+1,y])
        if y!=0 and self.image[x][y-1]=='1' and (x, y-1) not in self.visited:
            probes.append([x,y-1])
        if y!=len(self.image[0])-1 and self.image[x][y+1]=='1' and (x, y+1) not in self.visited:
            probes.append([x,y+1])
        return probes

    def edgedNeighbors(self, neighbors):
        result=[]
        for p in neighbors:
            x,y=p
            if x==0 or x==len(self.image)-1 or y==0 or y==len(self.image[0])-1 or self.image[x-1][y]=='0'\
                or self.image[x+1][y]=='0' or self.image[x][y-1]=='0' or self.image[x][y+1]=='0':
                result.append(p)

        return result

    def walkEdge(self, x,y):


        while True:
            # print x,y
            self.visited.add((x,y))
            if x<self.left:
                self.left=x
            elif x>self.right:
                self.right=x

            if y<self.up:
                self.up=y
            elif y> self.low:
                self.low=y

            # print self.left, self.right, self.up, self.low

            uN=self.unvisitedNeighbors(x,y)
            if not uN:
                return

            eN=self.edgedNeighbors(uN)

            if not eN:
                # print eN, x,y, uN
                uN=[p for k in uN for p in self.unvisitedNeighbors(*k)]
                eN=self.edgedNeighbors(uN)
                # print len(uN), len(eN), x,y

                if not eN:
                    return

            x,y=eN[0]

            for p in uN[1:]:
                self.walkEdge(*p)

if __name__ == '__main__':
    solution=Solution()
#     print solution.minArea([
#   "0010",
#   "0110",
#   "0100"
# ], 0, 2)

    for _ in xrange(1):

#         print solution.minArea([
#         "00000111111111011100000000000000000000",
#         "00001111111111111100000000000000000000",
#         "00000000111111110000000000000000000000",
#         "00000001111111110000000000000000000000",
#         "00000011111111110000000000000000000000",
#         "00000011111111110000000000000000000000",
#         "00000011101111110000000000000000000000",
#         "00000011111110000000000000000000000000",
#         "00000011111001000000000000000000000000",
#         "00000001111011000000000000000000000000",
#         "00000011111111000000000000000000000000",
#         "00000000111101000000000000000000000000",
#         "00000000011100000000000000000000000000",
#         "00000000011100000000000000000000000000",
#         "00000000011000000000000000000000000000",
#         "00000000000000000000000000000000000000"],
# 6,
# 15)
        print solution.minArea(["0010",
            "0110",
            "0100"],
            0,
            2)

        




            