class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            if nums[0] == 1:
                return 2
            else:
                return 1
            
        before = nums[0]
        i = 0
        count = 0
        if nums[i] >= 1 and nums[i] <= len(nums):
            temp = nums[i] - 1
            nums[i] = nums[nums[i] - 1]
            nums[temp] = temp + 1
            count += 1
            
        while i < len(nums) and nums[i] == i + 1:
            i += 1
            count += 1
        
        while count < len(nums):
            if nums[i] == before:
                i += 1
            elif nums[i] == i + 1:
                i += 1
                count += 1
            elif nums[i] >= 1 and nums[i] <= len(nums):
                before = nums[i]
                temp = nums[i] - 1
                nums[i] = nums[nums[i] - 1]
                nums[temp] = temp + 1
                count += 1
            else:
                i += 1
                
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        
        return len(nums) + 1
            
        


if __name__ == "__main__":
    yes = Solution()

    print(yes.firstMissingPositive([1,2,6,3,5,4]))
    