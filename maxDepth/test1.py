# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

            
if __name__ == "__main__":
    yes = Solution()
    node = TreeNode(3)
    node.left = TreeNode(1)
    node.right = TreeNode(2)
    print(yes.maxDepth(node))