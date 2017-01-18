'''
331. Verify Preorder Serialization of a Binary Tree
Total Accepted: 4306 Total Submissions: 13398 Difficulty: Medium

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #

For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false


Note: '#' is considered valid too.

we just need to count leaves.
when a node comes, it has to attach to some current leaf position, and as the nodes (and true leaves) are exhausted, there must be no leave postions open.
we start with 1 leaf position for the root to attach on, and when there is a non-empty node, the total open leave positions will increase by 1, and when 
there is a '#', it decreases the leaf position by 1.  And at any moment, there should be at least 1 open leaf position for the new comer to attach to, unless there is no new comers.
'''
class Solution(object):
    def isValidSerialization(self, preorder):
        preorder=preorder.split(',')
        leaves=1
        for node in preorder:
            if leaves==0:
                return False
            leaves-=(1 if node=='#' else -1)
        return leaves==0



