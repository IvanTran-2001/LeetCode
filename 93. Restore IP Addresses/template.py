import bisect
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count = 0
        for i in range(len(nums)):
            nums[i] = nums[i] % k
            if nums[i] == 0:
                count += 1
        
        if count > 1:
            return True
        
        nums.sort()
        
        
        start = count
        
        for i in range(start, len(nums)):
            if self.recurse(nums, k - i, i):
                return True
        
        return False

    def recurse(self, nums, start, target):
        
        end = bisect.bisect_right(nums, (target // 2), start + 1)
        for i in range(start, end):
            find = self.b_search(nums, target, i)
            if find != -1:
                return True
            
        return False
    
    def b_search(self, arr, target, start_index):
        left = start_index
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid

            elif arr[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1
        
        
if __name__ == "__main__":
    yes = Solution()

    print(yes.checkSubarraySum([23,2,4,6,7], 6))

