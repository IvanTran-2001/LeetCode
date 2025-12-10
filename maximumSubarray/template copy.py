class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        maximum_val = nums[0]
        value = 0
        
        for n in (nums):
            
            value += n
            
            if value > maximum_val:
                maximum_val = value
                
            if value <= 0:
                value = 0
        
        return maximum_val
                
            

if __name__ == "__main__":
    yes = Solution()

    print(yes.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))