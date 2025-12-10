class Solution(object):
    def __init__(self):
        self.new_array = [[]]
        
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
            
        for i in range(1, len(nums) + 1):
            self.recurse(0, len(nums), i, [], nums)

        return self.new_array
    
    def recurse(self, start, end, k, new_list, nums):
        if k == 0:
            self.new_array.append(new_list)
        else:
            if start + k - 1 <= end:
                for i in range(start, end):
                    self.recurse(i + 1, end, k - 1, new_list + [nums[i]], nums)

        
        
        
        
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.subsets([3,2,4,1]))

