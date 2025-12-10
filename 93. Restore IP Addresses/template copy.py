class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map = {0: -1}  # To handle the case where the sub-array starts from index 0
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            rem = sum % k

            if rem in map:
                if i - map[rem] > 1:
                    return True
            else:
                map[rem] = i

        return False
        
        
if __name__ == "__main__":
    yes = Solution()

    print(yes.checkSubarraySum([23,2,4,6,7], 6))

