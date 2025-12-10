from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]):
        node_dict = {}
        for desc in descriptions:

            if not(desc[0] in node_dict):
                node_dict[desc[0]] = TreeNode(desc[0])
            
            if not(desc[1] in node_dict):
                node_dict[desc[1]] = TreeNode(desc[1])

            if desc[2] == 1:
                node_dict[desc[0]].left = node_dict[desc[1]]
            else:
                node_dict[desc[0]].right = node_dict[desc[1]]
        
        for desc in descriptions:
            if desc[1] in node_dict:
                del node_dict[desc[1]]
        
        head = None
        
        for i in node_dict.values():
            head = i

        return head
    
if __name__ == "__main__":
    yes = Solution()
    print(yes.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]))

