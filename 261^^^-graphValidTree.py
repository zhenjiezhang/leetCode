'''
261. Graph Valid Tree
Total Accepted: 8073 Total Submissions: 26389 Difficulty: Medium

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Hint:

    Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree?
    According to the definition of tree on Wikipedia: "a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree."

    '''












'''
https://leetcode.com/discuss/52610/8-10-lines-union-find-dfs-and-bfs


There are so many different approaches and so many different ways to implement each. I find it hard to decide, so here are several :-)

In all of them, I check one of these tree characterizations:

    Has n-1 edges and is acyclic.
    Has n-1 edges and is connected.

Solution 1 ... Union-Find

The test cases are small and harmless, simple union-find suffices (runs in about 50~60 ms).

def validTree(self, n, edges):
    parent = range(n)
    def find(x):
        return x if parent[x] == x else find(parent[x])
    def union(xy):
        #就是edge里那俩去各找各妈，找到了看看是不是同一个妈，同一个妈就说明前面已经同过别的途径连起来了，不同的妈就设成同一个妈，连起来。
        x, y = map(find, xy)
        parent[x] = y
        return x != y
    return len(edges) == n-1 and all(map(union, edges))

A version without using all(...), to be closer to other programming languages:

def validTree(self, n, edges):
    parent = range(n)
    def find(x):
        return x if parent[x] == x else find(parent[x])
    for e in edges:
        x, y = map(find, e)
        if x == y:
            return False
        parent[x] = y
    return len(edges) == n - 1

A version checking len(edges) != n - 1 first, as parent = range(n) could fail for huge n:

def validTree(self, n, edges):
    if len(edges) != n - 1:
        return False
    parent = range(n)
    def find(x):
        return x if parent[x] == x else find(parent[x])
    def union(xy):
        x, y = map(find, xy)
        parent[x] = y
        return x != y
    return all(map(union, edges))



Solution 2 ... DFS

def validTree(self, n, edges):
    neighbors = {i: [] for i in range(n)}
    for v, w in edges:
        neighbors[v] += w,
        neighbors[w] += v,
    def visit(v):
        map(visit, neighbors.pop(v, []))
    visit(0)
    return len(edges) == n-1 and not neighbors




Or check the number of edges first, to be faster and to survive unreasonably huge n:





def validTree(self, n, edges):
    if len(edges) != n - 1:
        return False
    neighbors = {i: [] for i in range(n)}
    for v, w in edges:
        neighbors[v] += w,
        neighbors[w] += v,
    def visit(v):
        map(visit, neighbors.pop(v, []))
    visit(0)
    return not neighbors

For an iterative version, just replace the three "visit" lines with

    stack = [0]
    while stack:
        stack += neighbors.pop(stack.pop(), [])


Solution 3 ... BFS

Just like DFS above, but replace the three "visit" lines with

    queue = [0]
    for v in queue:
        queue += neighbors.pop(v, [])

or, since that is not guaranteed to work, the safer

    queue = collections.deque([0])
    while queue:
        queue.extend(neighbors.pop(queue.popleft(), []))



'''

from collections import deque
class Solution(object):
    def validTree(self, n, edges):
        d=deque([0])
        nodes={0}
        connections=[set() for _ in xrange(n)]
        for e in edges:
            if e[0]==e[1]:
                return False
            connections[e[0]].add(e[1])
            connections[e[1]].add(e[0])
        while d:
            for newNode in connections[d[0]]:
                connections[newNode].remove(d[0])
                if newNode in nodes:
                    return False
                d.append(newNode)
                nodes.add(newNode)
            d.popleft()
        return len(nodes)==n








    def validTreeOld(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if not edges:
            return n==1

        table=[[] for _ in xrange(n)]

        used=set()

        for e in edges:
            table[e[0]].append(e[1])
            table[e[1]].append(e[0])

        i=0
        while not table[i]:
            i+=1

        front={i}

        while front:
            newFront=set()
            for f in front:
                for c in table[f]:
                    if c in front or c in newFront:
                        return False
                    if c not in used:
                        newFront.add(c)

            used|=front
            front=newFront

        return len(used)==n

if __name__ == '__main__':
    s=Solution()
    print s.validTree(4, [[0,1],[2,3]])
    print s.validTree(5, [[0,1],[0,2],[2,3],[2,4]])
    print s.validTree(3, [[2,0],[2,1]])
