from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        checker = True
        num = nums[0]
        for i in range(1, len(nums)):
            if num > nums[i]:
                if not checker:
                    return False
                    
                checker = False
                
            num = nums[i]
        
        if nums[0] < nums[-1]:
            if checker:
                return True
            else:
                return False
            
        return True

if __name__ == "__main__":
    yes = Solution()

    print(yes.check([2,1,3,4]))

