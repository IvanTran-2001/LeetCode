import math
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        reverse = True
        result = [label]
        while label != 1:
            upper = math.floor(math.log(label, 2))
            lower = upper - 1
            
            label = label//2
            if reverse:
                result.append(2**upper - 1 - (label - 2**lower))
            else:
                result.append(label)
            
            reverse = not reverse
            
        
        return result[::-1]
            

if __name__ == "__main__":
    yes = Solution()

    print(yes.pathInZigZagTree(13))

