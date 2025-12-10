class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        new_array = []
        start = 0
        count = 1
        
        
        for i in range(1, len(nums)):
            if nums[start] != nums[i]:
                new_array.append(count)
                start = i
                count = 1
            else:
                count += 1
        
        if not new_array:
            return len(nums)
        
        new_array.append(count)
        
        i = 0
        count = 0
        total = 0
        maxi = 0
        while i < len(new_array):
            if count > k:
                maxi = max(maxi, total)
                total -= new_array[i - k - 1]
                
                total += new_array[i]
                
            else:
                total += new_array[i]
                count += 1
            
            i += 1
            
        if k >= len(new_array) - 1:
            return total
        
        if i - k - 1 != 1 and nums[start] == nums[0]:
            total += new_array[0]
        
        maxi = max(maxi, total)
        
        return maxi
            
if __name__ == "__main__":
    yes = Solution()

    print(yes.maximumLength([38,40,38,40], 1))

