from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = 0
        start = 0
        while i < len(nums) and k > 0:
            if nums[i] % 2 == 1:
                k -= 1
            i += 1
        
        if k != 0:
            return 0
        
        count = 0
        memory = 1
            
        while i < len(nums):
            while start < len(nums) and nums[start] % 2 == 0:
                memory += 1
                start += 1
            
            count += memory
            
            while i < len(nums) and nums[i] % 2 == 0:
                i += 1
                count += memory
            
            memory = 1
            start += 1
            i += 1
        
        if nums[-1] % 2 == 1:
            while start < len(nums) and nums[start] % 2 == 0:
                memory += 1
                start += 1
            
            count += memory
        
        return count

if __name__ == "__main__":
    yes = Solution()

    print(yes.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 1))

