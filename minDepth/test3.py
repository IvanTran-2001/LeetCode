# Definition for a binary tree node.
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        num = 1
        next = [root]
        length = 1
        while True:
            temp = []
            for i in range(length):
                node = next[-i-1]
                length -= 1

                if not node.left and not node.right:
                    return num
                else:
                    if node.left:
                        temp.append(node.left)
                        length += 1
                    
                    if node.right:
                        temp.append(node.right)
                        length += 1

            next = temp
            num += 1