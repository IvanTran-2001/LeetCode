class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        array_of_water = [0] * len(height)

        start = 0
        before = 0

        for i in range(1, len(height)):
                
            minimal = min(height[i], height[start])
            if height[before] < minimal:
                
                for j in range(start+1, i):
                    if height[j] + array_of_water[j] < minimal:
                        array_of_water[j] = minimal - height[j]
                        
            if height[start] <= height[i]:
                start = i
                
            before = i
                    
        return sum(array_of_water)
            
            
            
            
            

if __name__ == "__main__":
    yes = Solution()

    print(yes.trap([2,6,3,8,2,7,2,5,0]))