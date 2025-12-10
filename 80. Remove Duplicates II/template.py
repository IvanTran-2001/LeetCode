class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums) == 1:
            return 1
        
        count = 1
        before = nums[0]
        dead = 0
        for i in range(1, len(nums)):
            if before != nums[i]:
                before = nums[i]
                count = 1
                dead += 1
            else:
                if count == 2:
                    ''
                else:
                    count += 1
                    dead += 1
            
            nums[dead] = nums[i]
            
        return dead + 1
        # return nums[:dead + 1]

if __name__ == "__main__":
    yes = Solution()

    print(yes.removeDuplicates([0,0,1,1,1,1,2,3,3]))

