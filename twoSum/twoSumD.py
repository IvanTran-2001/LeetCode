class Solution(object):
    def twoSum(self, nums, target):


        for i in range(len(nums)):
            nums[i] = [i,nums[i]]
        nums = sorted(nums, key=lambda x: x[1])

        for i in range(len(nums)):

            value = self.binary_search(nums, target - nums[i][1], i)

            if value != -1:
                return [nums[i][0], nums[value][0]]
        
        return -1
        

    def binary_search(self, arr, target, i):

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid][1] == target:

                if mid == i:
                    return -1
                else:
                    return mid
                
            elif arr[mid][1] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    nums = [3,2,4]
    roman = Solution()
    print(roman.twoSum(nums, 6))