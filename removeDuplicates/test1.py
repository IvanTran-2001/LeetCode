class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums:
            k = 1
            b4 = nums[0]

            for i in nums:
                if b4 < i:
                    k += 1
                    b4 = i
                    nums[k - 1] = b4
            return k
        else:
            return 0

if __name__ == "__main__":
    yes = Solution()

    print(yes.removeDuplicates([1,1,2]))