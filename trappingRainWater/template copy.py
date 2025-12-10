class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        start = 0
        end = len(height) - 1
        total = 0
        start_max = start
        end_max = end
        a = 0
        b = 0
        
        while start < end:
            if height[start] < height[end]:
                start += 1
                a = height[start]
                
                if height[start] < height[start_max]:
                    total += height[start_max] - height[start]
                else:
                    start_max = start

            else:
                end -= 1
                b = height[end]
                if height[end] < height[end_max]:
                    total += height[end_max] - height[end]
                else:
                    end_max = end
                    
        return total
            
            
            
            
            
            
            

if __name__ == "__main__":
    yes = Solution()

    print(yes.trap([0,1,0,2,1,0,1,3,2,1,2,1]))