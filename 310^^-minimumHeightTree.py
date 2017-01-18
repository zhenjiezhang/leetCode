'''
310. Minimum Height Trees
Total Accepted: 6878 Total Submissions: 26637 Difficulty: Medium

For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3

return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5

return [3, 4]

Hint:

    How many MHTs can a graph have at most?

Note:

(1) According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”

(2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf. 

另一个办法，从每一个分叉点出发，寻找离它最远的叶子，这样可以recurse。用缓存来加速。

'''


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n==1:
            return [0]

        connectedNodes=[set() for i in xrange(n)]
        for e in edges:
            connectedNodes[e[0]].add(e[1])
            connectedNodes[e[1]].add(e[0])

        leaves=[]
        for i in xrange(len(connectedNodes)):
            if len(connectedNodes[i])==1:
                leaves.append(i)

        while len(leaves)>2 or (len(leaves)==2 and leaves[1] not in connectedNodes[leaves[0]]):
            newLeaves=[]
            for l in leaves:
                parent=connectedNodes[l].pop()
                connectedNodes[parent].remove(l)
                if len(connectedNodes[parent])==1:
                    newLeaves.append(parent)

            leaves=newLeaves

        return leaves

if __name__=='__main__':
    print Solution().findMinHeightTrees(1,[])


