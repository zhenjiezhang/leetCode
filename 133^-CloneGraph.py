'''
133. Clone Graph
Total Accepted: 57385 Total Submissions: 233231 Difficulty: Medium

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

OJ's undirected graph serialization:

Nodes are labeled uniquely.
We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

    First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
    Second node is labeled as 1. Connect node 1 to node 2.
    Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.

Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

         '''

         # Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        
        sourceNodes=[node]
        distNodes={node.label:UndirectedGraphNode(node.label)}
        workingNode=0

        while workingNode < len(sourceNodes):
            for nd in sourceNodes[workingNode].neighbors:
                if nd.label not in distNodes:
                    sourceNodes.append(nd)
                    distNodes[nd.label]=UndirectedGraphNode(nd.label)
            distNodes[sourceNodes[workingNode].label].neighbors=[distNodes[nd.label] for nd in sourceNodes[workingNode].neighbors]
            workingNode+=1
        return distNodes[node.label]

if __name__ == '__main__':
    solution=Solution()
    node=UndirectedGraphNode("1")
    node.neighbors=[UndirectedGraphNode('2')]
    print solution.cloneGraph(node)

