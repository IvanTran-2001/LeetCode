class Solution(object):

    def nextPermutation(self, nums):
        start = -1
        end = -1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                start = i-1
                end = i
            
            elif start != -1 and nums[i] <= nums[end] and nums[i] > nums[start]:
                end = i
        
        if start == -1:
            nums = nums.reverse()
        else:
            nums[start], nums[end] = nums[end], nums[start]
        
            nums[start + 1:] = reversed(nums[start + 1:])
        
        return nums
            
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.nextPermutation([1,5,1,3,2]))