# Definition for singly-linked list.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.recur(nums, TreeNode())

    def recur(self, nums, node):
        length = len(nums)
        half = (length+1)//2 - 1
        if length == 0:
            return None
        else:
            node.val = (nums[half])
            if length != 1:
                if half != 0:
                    node.left = TreeNode()
                    self.recur(nums[0:half], node.left)
                if half+1 != length:
                    node.right = TreeNode()
                    self.recur(nums[half+1:], node.right)

            return node



if __name__ == "__main__":
    yes = Solution()
    print(yes.sortedArrayToBST([-10,-3,0,5,9]).val)

    


        
        

            
            
