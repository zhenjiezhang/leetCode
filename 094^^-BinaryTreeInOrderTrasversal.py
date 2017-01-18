'''
in-order transversal


shortter version:

public List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> res = new LinkedList<Integer>();
    if (root == null) return res;

    Stack<TreeNode> stack = new Stack<TreeNode>();
    TreeNode cur = root;
    while (cur != null || !stack.isEmpty()) { 
        while (cur != null) {// Travel to the left leaf
            stack.push(cur);
            cur = cur.left;             
        }        
        cur = stack.pop(); // Backtracking to higher level node A
        res.add(cur.val);  // Add the node to the result list
        cur = cur.right;   // Switch to A'right branch
    }
    return res;
}
'''


'''
Morris traversal does not use extra space (no stack):


Inorder Tree Traversal without recursion and without stack!

Using Morris Traversal, we can traverse the tree without using stack and recursion. 
The idea of Morris Traversal is based on Threaded Binary Tree. In this traversal, we first create links
 to Inorder successor and print the data using these links, and finally revert the changes to restore original tree.

1. Initialize current as root 
2. While current is not NULL
   If current does not have left child
      a) Print current’s data
      b) Go to the right, i.e., current = current->right
   Else
      a) Make current as right child of the rightmost node in current's left subtree
      b) Go to this left child, i.e., current = current->left

Although the tree is modified through the traversal, it is reverted back to its original shape after the completion. 
Unlike Stack based traversal, no extra space is required for this traversal.


vector<int> inorderTraversal(TreeNode* root) {

    vector<int> v;
    if(!root) return v;
    TreeNode* temp = root, *prev;
    while(temp){
        if(!temp->left){
            v.push_back(temp->val);
            temp = temp->right;
        }else{
            prev = temp->left;
            while(prev->right&&(prev->right != temp))
                prev = prev->right;
            if(!prev->right){
                prev->right = temp;
                temp = temp->left;
            }else{
                v.push_back(temp->val);
                prev->right = NULL;
                temp = temp->right;
            }
        }
    }
}
'''
#recurse is trivial.  Try iteration

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        nodeStack=[]
        results=[]
        node=root

        while node:
            if node.left:
                nodeStack.append(node)
                node=node.left
                continue
            else:
                results.append(node.val)
                if node.right:
                    node=node.right
                    continue
                elif nodeStack:
                    node=nodeStack.pop()
                    while node.right is None and nodeStack:
                        results.append(node.val)
                        node=nodeStack.pop()
                    if node.right:
                        results.append(node.val)                        
                        node=node.right
                        continue
                    else:
                        results.append(node.val)
                        return results


                else:
                    return results
        return results

if __name__ == '__main__':
    solution=Solution()
    print solution.inorderTraversal({})
