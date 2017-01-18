'''
private void getLeaves(List<List<Integer>> ret, List<TreeNode> list) {
    List<TreeNode> leaves = new ArrayList<TreeNode>();
    List<Integer> values = new ArrayList<Integer>();
    Iterator<TreeNode> it = list.iterator();
    TreeNode node;
    while(it.hasNext()) {
        node = it.next();
        values.add(node.val);
        if(node.left != null) {
            leaves.add(node.left);
        }
        if(node.right != null) {
            leaves.add(node.right);
        }
    }
    if(!leaves.isEmpty()) {
        getLeaves(ret, leaves);
    }
    ret.add(values);
}
public List<List<Integer>> levelOrderBottom(TreeNode root) {
    List<List<Integer>> ret = new ArrayList<List<Integer>>();
    if(root != null) {
        List<TreeNode> list = new ArrayList<TreeNode>();
        list.add(root);
        getLeaves(ret, list);

    }
    return ret;
}
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if not root:
    		return []

        buf=[root]
        nextLevel=[]
        result=[]

        while buf:
        	val=[]
        	for node in buf:
        		val.append(node.val)
        		if node.left:
        			nextLevel.append(node.left)
        		if node.right:
        			nextLevel.append(node.right)
        	result.append(val)
        	buf=nextLevel
        	nextLevel=[]
        return result[::-1]