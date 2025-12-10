class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tList = []
        if not root:
            return []
        
        if root.left:
            tList += self.postorderTraversal(root.left)
        
        if root.right:
            tList += self.postorderTraversal(root.right)
            
        return tList + [root.val]

if __name__ == "__main__":
    # Creating nodes
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)

    # Constructing the tree
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.left = node8
    node4.right = node9
    
    yes = Solution()
    no = yes.postorderTraversal(node1)
    print(no)
        
        
        
        
        