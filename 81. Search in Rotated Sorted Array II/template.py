class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start = 0
        end = len(nums) - 1
        side = 1
        while start < end:
            yes = nums[start: end+1]
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                side = 0
                start = mid + 1
            elif nums[mid] == nums[start] and side == 1:
                start += 1
            elif nums[mid] == nums[end]:
                end -= 1
            else:
                side = 1
                end = mid
        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            temp = mid + start
            
            if temp >= len(nums):
                temp -= len(nums)
            
            if nums[temp] == target:
                return True
            elif nums[temp] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
                

if __name__ == "__main__":
    yes = Solution()

    print(yes.search([1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 0))

