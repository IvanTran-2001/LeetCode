from typing import List
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        count = 0
        i = 0
        k_ = 0
        before = 1
        array = [1] * k
        
        while i < len(nums):
            if nums[i] != before:
                k = 0
                count += 1
            else:
                k += 1
            
        return count

if __name__ == "__main__":
    yes = Solution()

    print(yes.minKBitFlips([0,1,0], 1))

