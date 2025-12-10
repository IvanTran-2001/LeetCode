# Definition for a binary tree node.
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.height(root, 1)
        
    def height(self, root, height):
        if not root: return 0

        left, right = self.height(root.left, height + 1), self.height(root.right, height + 1)

        if left == 0 and right == 0:
            return (height)
        if left == 0:
            return right
        if right == 0:
            return left
        return min(left, right)

            
        
        
if __name__ == "__main__":
    test = Solution()