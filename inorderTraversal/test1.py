# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []

        elif root.left == None:
            return [root.val] + self.inorderTraversal(root.right) 
        
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
        
if __name__ == "__main__":
    yes = Solution()
    node = TreeNode(3)
    node.left = TreeNode(1)
    node.right = TreeNode(2)
    print(yes.inorderTraversal(node))