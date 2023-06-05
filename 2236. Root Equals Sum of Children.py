class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):#funker ikk ei pycharm pga left og right type noen
        self.val = val
        self.left = left
        self.right = right

root = TreeNode([10,4,6])

class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root.left.val + root.right.val ==root.val:
            return True
        else:
            return False
print(Solution().checkTree(root))