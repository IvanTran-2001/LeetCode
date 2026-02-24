import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from CusNode import list_to_binary_tree

class Solution:
    def sumRootToLeaf(self, root, num=0):
        if not root:
            return 0
        num = (num << 1) | root.val
        if not root.left and not root.right:  # leaf node — return the completed number
            return num
        return self.sumRootToLeaf(root.left, num) + self.sumRootToLeaf(root.right, num)

if __name__ == "__main__":
    yes = Solution()
    list = list_to_binary_tree([1,0,1,0,1,0,1])
    print(yes.sumRootToLeaf(list))

