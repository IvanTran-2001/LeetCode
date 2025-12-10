# Definition for a binary tree node.
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        maxArea = 0
        restrict = max(height)
        
        while (start < end) and ((end - start) * restrict > maxArea):
            minHeight = min(height[start], height[end])
            area = minHeight * (end - start)
                
            if maxArea < area:
                maxArea = area
            
            if height[start] > height[end]:
                end -= 1
            else:
                start +=1
        
        return maxArea
            
            
            
        
        

            
if __name__ == "__main__":
    yes = Solution()
    print(yes.maxArea([2,3,10,5,7,8,9]))
    