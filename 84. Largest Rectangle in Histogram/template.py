class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_height = 0
        for i in range(len(heights)):
            
            if heights[i] == 0:
                continue
            
            min_height = heights[i]
            max_height = max(min_height, max_height)
            
            if min_height * (len(heights) - i) < max_height:
                continue
            
            for j in range(i + 1, len(heights)):
                min_height = min(min_height, heights[j])
                
                if min_height == 0:
                    break
                
                max_height = max(max_height, min_height*(j - i + 1))
        
        return max_height
            
            

if __name__ == "__main__":
    yes = Solution()

    print(yes.largestRectangleArea([2,1,5,6,2,3]
))

