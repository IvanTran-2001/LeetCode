class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zero = 0
        i = 0
        maxSub = 0
        length = len(nums)
        while i < length:
            if nums[i] == 1:
                once = True
                temp = 0
                while i < length and nums[i] == 1:
                    i+= 1
                    temp += 1
                    if once and i < length and nums[i] == 0:
                        once = False
                        zero = i
                        i += 1
                        
                if temp > maxSub:
                    maxSub = temp
                    if maxSub > length - i + 1:
                        break
                if not once:
                    i = zero
                    once = True

            i += 1

        if maxSub == length:
            maxSub -= 1
        
        return maxSub


if __name__ == "__main__":
    yes = Solution()

    print(yes.longestSubarray([1,0,1,1,1,1,1,1,0,1,1,1,1,1]))