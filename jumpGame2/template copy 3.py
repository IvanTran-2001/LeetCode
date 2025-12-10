class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums or len(nums) == 1:
            return 0
        if len(nums) == 2 or nums[0] >= len(nums) - 1:
            return 1
        
        count = 2
        
        max_index = 0
        for i in range(1, nums[0] + 1):
            
            if nums[i] + i >= len(nums) - 1:
                return count
            if i + nums[i] >= len(nums) - 1:
                return count 
            if i + nums[i] > max_index + nums[max_index]:
                max_index = i
        
        i = nums[0]
        while i < len(nums) - 2:
            count += 1
            # max_loop =  nums[max_index] - (i - max_index)
            for j in range(1, nums[max_index] - (i - max_index) + 1):
                if i + j >= len(nums) - 1:
                    return count
                if i + j + nums[i + j] >= len(nums) - 1:
                    return count 
                elif i + j + nums[i + j] > max_index + nums[max_index]:
                    max_index = i + j
                
            i += nums[i]
        return count
    
    
if __name__ == "__main__":
    yes = Solution()
    
    print(yes.jump([2,0,8,0,3,4,7,5,6,1,0,0,5,9,7,5,3,6]))
    
    array_list = [
    [[1,1,1,1], 3],
    [[1,1,1,2,1], 4],
    [[1,1,2,1,1], 3],
    [[2,0,2,0,1], 2],
    [[9,8,2,2,0,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5], 3],
    [[1,2,0,1], 2],
    [[2,3,1,1,4], 2]]
    count = 1
    for i in array_list:
        print(count, yes.jump(i[0]) == i[1])
        count += 1