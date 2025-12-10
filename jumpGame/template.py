class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_index = nums[0]
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                if max_index <= i:
                    return False
            elif i + nums[i] > max_index:
                max_index = i + nums[i]
        
        return True
            

if __name__ == "__main__":
    yes = Solution()

    print(yes.canJump([2,5,0,0]))