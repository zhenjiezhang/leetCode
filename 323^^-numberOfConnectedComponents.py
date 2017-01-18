'''
323. Number of Connected Components in an Undirected Graph
Total Accepted: 4017 Total Submissions: 9355 Difficulty: Medium

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

     0          3
     |          |
     1 --- 2    4

Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:

     0           4
     |           |
     1 --- 2 --- 3

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1. 


'''

class Solution(object):
    # union find solution

    def countComponents(self, n, edges):
        origins=range(n)
        for nd1, nd2 in edges:
            while origins[nd2]!=nd2:
                nd2=origins[nd2]
            while origins[nd1]!=nd1:
                nd1=origins[nd1]
            origins[nd2]=nd1

        return len([i for i in xrange(n) if origins[i]==i])



    def countComponentsOpt(self, n, edges):
        origins=range(n)
        for nd1, nd2 in edges:
            root1=nd1
            root2=nd2
            while origins[root2]!=root2:
                root2=origins[root2]
            while origins[root1]!=root1:
                tmp=origins[root1]
                # critical to improving speed
                # otherwise this loop could be simpler, identical to the loop for root2
                origins[root1]=root2
                root1=tmp
            # critical to improving speed
            origins[nd2]=root2
            origins[root1]=root2
        return len([i for i in xrange(n) if origins[i]==i])



    def countComponentsOld(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        table=[set() for _ in xrange(n)]
        for e in edges:
            table[e[0]].add(e[1])
            table[e[1]].add(e[0])

        used=set()

        numComp=0

        for i in xrange(n):
            if i not in used:
                used.add(i)

                currentComponent=set([i])
                front=table[i]

                while front:
                    nextFront=set()
                    for f in front:
                        currentComponent.add(f)
                        nextFront|=table[f]
                    nextFront-=currentComponent
                    front=nextFront

                used |=currentComponent
                numComp+=1
        print used

        return numComp

if __name__ == '__main__':
    solution=Solution()
    print solution.countComponents(4,[[2,3],[1,2],[1,3]])
    print solution.countComponents(8,[[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5],[5,1],[6,4]])





