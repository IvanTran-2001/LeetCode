class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        end = len(nums) -1
        if not nums or end == 0:
            return 0
        if end == 1 or nums[0] >= end:
            return 1
        
        index = 0
        count = 0
        
        while end > 0:
            last = 0
            for i in range(1, end + 1):
                
                tIndex = end -i
                term = i - nums[tIndex]
                
                if term <= 0:
                    last = tIndex
                    
            count += 1
                    
            end = last
            index += 1
            
        return count
            
if __name__ == "__main__":
    yes = Solution()

    print(yes.jump([2,3,1,1,4]))