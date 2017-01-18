'''
Same thought but much cleaner!!!

这个就是每遇到一个右节点(每一个p都有可能是，当p>preorder[i]的时候)，就去找到相应的左结点(low点)，然后右节点的右边的值如是小于左结点的值的话，当然就false啦。
public boolean verifyPreorder(int[] preorder) {
    int low = Integer.MIN_VALUE, i = -1;
    for (int p : preorder) {
        if (p < low)
            return false;
        while (i >= 0 && p > preorder[i])
            low = preorder[i--];
        preorder[++i] = p;
    }
    return true;
}

implement this in python, then implement my recursive version. see which is faster:

for each round, scan and find the first element > root, set this as right, and make sure element after right all > root (or pass the root value to the right tree when doing recurse and check there).  
the left tree is between root and right.  recurse on the left and right trees.

'''

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """

        probe=1
        # find the first left branch
        while probe < len(preorder) and preorder[probe]>preorder[probe-1]:
            probe+=1
        if probe ==len(preorder):
            return True

        rootWithLeft=probe-1

        leftLimit=preorder[rootWithLeft-1] if rootWithLeft>0 else -float('inf')

        connectPoint=probe-1

        while probe<len(preorder):

            if preorder[probe] < preorder [connectPoint]:
                if preorder[probe]<leftLimit:
                    return False

                preorder[connectPoint+1]=preorder[probe]
                connectPoint+=1
                probe+=1
            else:
                while connectPoint>rootWithLeft and preorder[connectPoint-1] < preorder[probe]:
                    connectPoint-=1

                if connectPoint==rootWithLeft:
                    leftLimit=preorder[connectPoint]
                    while probe < len(preorder) and preorder[probe]>preorder[probe-1]:
                        probe+=1
                    if probe ==len(preorder):
                        return True

                    connectPoint=rootWithLeft=probe-1
                    leftLimit=max(preorder[rootWithLeft-1], leftLimit)
                else:
                    probe+=1
                    leftLimit=preorder[connectPoint]

        return True






if __name__ == '__main__':
    s=Solution()
    print s.verifyPreorder([8,5,4,3,7,20,12,9,10,11,18])
    print s.verifyPreorder([4,2,3,1])
