import math
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
    
        def find_path(label):
            
            if label == 1:
                return [1]
            
            upper = math.floor(math.log2(label))
            lower = (upper - 1)
            upper = 1 << upper
            lower = 1 << lower
            parent = (label//2)
            
            parent = int(upper - 1 - (parent - lower))

            return find_path(parent) + [label]
        
        return find_path(label)

if __name__ == "__main__":
    yes = Solution()
    print(yes.pathInZigZagTree(15))