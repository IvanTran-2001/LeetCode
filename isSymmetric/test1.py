# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left == None and root.right == None:
            return True
        
        return self.sys(root.left, root.right)

    def sys(self, left, right):
        if left == None and right == None:
            return True
        if left != None and right == None:
            return False
        if right != None and left == None:
            return False

        if left.val != right.val:
            return False
        else:
            return self.sys(left.left, right.right) and self.sys(left.right, right.left)

            
if __name__ == "__main__":
    yes = Solution()
    node = TreeNode(3)
    node.left = TreeNode(1)
    node.right = TreeNode(2)
    print(yes.isSymmetric(node))