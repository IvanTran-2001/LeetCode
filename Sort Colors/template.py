class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = {0: 0, 1: 0, 2:0}
        for i in nums:
            if i in count:
                count[i] += 1
                
        counter = 0
        for i in count:
            for _ in range(count[i]):
                nums[counter] = i
                counter += 1
        
        return nums
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.sortColors([2,0,2,1,1,0]))

