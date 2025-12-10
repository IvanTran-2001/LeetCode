class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return (self.height(root) != -1)

        
    
    def height(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (root is None): 
            return 0

        left, right = self.height(root.left), self.height(root.right)

        if (left < 0 | right < 0 | abs(left-right) > 1): 
            return -1

        return max(left, right) + 1