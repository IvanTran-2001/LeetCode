# Definition for a binary tree node.
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height) - 1
        maxArea = 0
        restrict = max(height)
        
        for i,n in enumerate(height):
            
            tempLength = length
            while (i < tempLength) and ((tempLength-i)*restrict > maxArea) :
                minHeight = min(height[i], height[tempLength])
                area = minHeight * (tempLength - i)
                
                if maxArea < area:
                    maxArea = area
                    
                tempLength -= 1
            
        
        return maxArea
                
            
        
        

            
if __name__ == "__main__":
    yes = Solution()
    print(yes.maxArea([2,3,10,5,7,8,9]))
    