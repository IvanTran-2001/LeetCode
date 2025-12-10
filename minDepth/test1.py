# Definition for a binary tree node.
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
    def height(self, root, height):
        if not root: return 0

        left, right = self.height(root.left, height + 1), self.height(root.right, height + 1)

        if left == 0 and right == 0:
            return -1*(height)
        
        if left < 0 or right < 0:
            if left >= 0:
                return right
            elif right >= 0:
                return left
            
            return max(left, right)
        
        return 0
            
        
        
if __name__ == "__main__":
    test = Solution()