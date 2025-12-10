class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        length = 0

        for i in nums:
            if i == 0:
                nums[length] = index
                length += 1
            index += 1
            
        maxSub = 0
        if length > 0:
            if length > 1:
                temp = nums[0] + (nums[1] - (nums[0]+1))
            else:
                return nums[0] + (index - (nums[0]+1))

            if temp > maxSub:
                    maxSub = temp

            for i in range(length-2):
                temp = nums[i+1] - (nums[i]+1) + (nums[i+2] - (nums[i+1]+1))
                if temp > maxSub:
                    maxSub = temp
                    if index - i < maxSub:
                        break
            
            temp = nums[length-1] - (nums[length-2]+1) + (index - (nums[length-1]+1))

            if temp > maxSub:
                return temp

        else:
            return index-1

        return maxSub

            
if __name__ == "__main__":
    yes = Solution()

    print(yes.longestSubarray([1,1,0,1]))