# Definition for a binary tree node.
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root: return False
        val = targetSum-root.val
        if (val) == 0:
            if not root.left and not root.right: return True

        return self.hasPathSum(root.left, val) or self.hasPathSum(root.right, val)
   
if __name__ == "__main__":
    test = Solution()