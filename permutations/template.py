class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp = []
        if len(nums) == 1:
            return [nums]
        
        for i in range(len(nums)):
            for j in self.permute(nums[:i] + nums[i+1:]):
                temp.append([nums[i]] + j)
                
        return temp
        
            

if __name__ == "__main__":
    yes = Solution()

    print(yes.permute([1,2,3]))