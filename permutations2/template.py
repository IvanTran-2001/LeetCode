class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permute(nums, len(nums))
    
    def permute(self, nums, max_length):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp = []
        if len(nums) == 1:
            return [nums]
        
        for i in range(len(nums)):
            for j in self.permute(nums[:i] + nums[i+1:], max_length):
                if len(nums) == max_length:
                    if [nums[i]] + j in temp:
                        continue
                temp.append([nums[i]] + j)
                
        return temp
        
            

if __name__ == "__main__":
    yes = Solution()

    print(yes.permuteUnique([1,1,3]))