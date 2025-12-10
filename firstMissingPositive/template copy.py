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
            
        back = len(nums) - 1
        position = 0
        
        for _ in range(len(nums)):
            if nums[position] > position and nums[position] <= back:
                if nums[position] == position + 1:
                    position += 1
                else:
                    if nums[position] == nums[nums[position] - 1]:
                        temp = nums[position]
                        nums[position] = nums[back]
                        nums[back] = temp
                        back -= 1
                    else:
                        temp = nums[position]
                        nums[position] = nums[nums[position] - 1] 
                        nums[temp - 1] = temp
            else:
                temp = nums[position]
                nums[position] = nums[back]
                nums[back] = temp
                back -= 1
                
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        
        return len(nums) + 1
            
        


if __name__ == "__main__":
    yes = Solution()

    print(yes.firstMissingPositive([39,8,43,12,38,11,-9,12,34,20,44,32,10,22,38,9,45,26,-4,2,1,3,3,20,38,17,20,25,41,35,37,18,37,34,24,29,39,9,36,28,23,18,-2,28,34,30]))
    