# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        else:
            if p != None and q == None:
                return False
            elif q != None and p == None:
                return False
            
        return (p.val == q.va) and (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))

if __name__ == "__main__":
    yes = Solution()
    print(yes.isSameTree("1010", "1011"))