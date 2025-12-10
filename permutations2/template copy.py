class Solution(object):
    def permuteUnique(self, nums):
        return self.permute(sorted(nums))
        
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp = []
        
        if len(nums) == 1:
            return [nums]
        
        before = None
        
        for i in range(len(nums)):
            if nums[i] == before:
                continue
            
            for j in self.permute(nums[:i] + nums[i+1:]):
                temp.append([nums[i]] + j)
                    
            before = nums[i]
                
        return temp
        
            

if __name__ == "__main__":
    yes = Solution()

    print(yes.permuteUnique([1,1,3]))