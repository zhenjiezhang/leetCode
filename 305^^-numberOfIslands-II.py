'''
305. Number of Islands II
Total Accepted: 3719 Total Submissions: 11133 Difficulty: Hard

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0

Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0

Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0

Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0

Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0

We return the result as an array: [1, 1, 2, 3]

Challenge:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
'''
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        #set to 0 to simplify code with the [-1] operation
        result=[0]

        islands=[]

        pos2island=[[-1]*n for _ in xrange(m)]

        for p in positions:
            #find out how many islands are neighboring the new land
            neighborIslandsIndexes=set()
            if p[0]!=0 and pos2island[p[0]-1][p[1]] >=0 :
                neighborIslandsIndexes.add(pos2island[p[0]-1][p[1]])
            if p[0]!=m-1 and pos2island[p[0]+1][p[1]] >=0:
                neighborIslandsIndexes.add(pos2island[p[0]+1][p[1]])
            if p[1]!=0 and pos2island[p[0]][p[1]-1] >=0 :
                neighborIslandsIndexes.add(pos2island[p[0]][p[1]-1])
            if p[1]!=n-1 and pos2island[p[0]][p[1]+1] >=0:
                neighborIslandsIndexes.add(pos2island[p[0]][p[1]+1])

            result.append(result[-1]+1-len(neighborIslandsIndexes))

            #case 0 is simple
            if len(neighborIslandsIndexes)==0:
                islands.append([p])
                pos2island[p[0]][p[1]]=len(islands)-1
            #case 1,2,3,4, we may need to merge multiple islands
            else:
                #find out which island is largest
                largestNeighborIsland_Index=-1
                largestNeighborIslandSize=0
                for i in neighborIslandsIndexes:
                    if len(islands[i])>largestNeighborIslandSize:
                        largestNeighborIsland_Index=i
                        largestNeighborIslandSize=len(islands[i])

                #add the new land to the largest island
                pos2island[p[0]][p[1]]=largestNeighborIsland_Index
                islands[largestNeighborIsland_Index].append(p)

                #add the lands of all other neighboring islands to the largest one
                neighborIslandsIndexes.remove(largestNeighborIsland_Index)
                for i in neighborIslandsIndexes:
                    for l in islands[i]:
                        pos2island[l[0]][l[1]]=largestNeighborIsland_Index
                    islands[largestNeighborIsland_Index].extend(islands[i])

        return result[1:]

if __name__ == '__main__':
    solution=Solution()
    print solution.numIslands2(m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]])


