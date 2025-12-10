class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        toSwap = []
        k = 0
        length = len(nums)

        while nums:
            if nums[length -1] == val:
                del nums[length -1]
                length -= 1
            else:
                break

        if not nums:
            return k

        for i in range(length):
            if nums[-i-1] == val:
                toSwap.append(-i-1)
                k += 1
        
        print(toSwap)
        for i in range(length):
            if toSwap:
                ok = -(i + 1)
                if nums[ok] != val:
                    index = toSwap.pop()
                    nums[ok], nums[index] = nums[index], nums[ok]
                else:
                    toSwap.pop(0)
            else:
                break

        print(nums)
        print(k)
        print(length - k)
        return length - k
    
if __name__ == "__main__":
    nums = [4,2,0,2,2,1,4,4,1,4,3,2]
    yes = Solution()
    yes.removeElement(nums , 4)