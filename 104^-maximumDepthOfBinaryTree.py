'''
104. Maximum Depth of Binary Tree
Total Accepted: 114057 Total Submissions: 243566 Difficulty: Easy

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Interesting BFS

int maxDepth(TreeNode* root)
{
    if (!root)
        return 0;
    queue<TreeNode*> mp;
    int dp = 1;
    mp.push(root);
    mp.push(0);//Separator: end of current layer.
    while (!mp.empty())
    {
        TreeNode* t = mp.front();
        mp.pop();
        if (t)
        {
            if (t->left)
                mp.push(t->left);
            if (t->right)
                mp.push(t->right);
        }
        else if (!mp.empty())  /*t==0 meet the separator, but not the last element of 'mp'.*/
        {
            mp.push(0);
            ++dp;
        }
    }
    return dp;
}
'''

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if not root:
        	return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))