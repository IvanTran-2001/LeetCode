class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] = {i:nums[i]}

        nums = sorted(nums, key=lambda x: list(x.values())[0])

        value = 0
        index = -1

        for i in range(len(nums)):

            value = self.binary_search(nums, target - list(nums[i].values())[0], i)

            if value != -1:
                index = i
                break
        
        return [list(nums[index].keys())[0], list(nums[value].keys())[0]]
        

    def binary_search(self, arr, target, i):

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if list(arr[mid].values())[0] == target:
                if mid == i:
                    return -1
                else:
                    return mid
            elif list(arr[mid].values())[0] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == "__main__":
    nums = [3,2,4]
    roman = Solution()
    print(roman.twoSum(nums, 6))