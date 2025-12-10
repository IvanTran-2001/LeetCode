class Solution:
    
    def containsNearbyDuplicate(self, nums, k) -> bool:
        n = len(nums)
        s = set()
        if n < k + 1:
            for i in range(n):
                if nums[i] in s:
                    return True
                
                s.add(nums[i])
            return False
        
        for i in range(k+1):
            if nums[i] in s:
                return True
            
            s.add(nums[i])
        
        for i in range(k+1, n):
            
            j = i - k-1
            
            s.remove(nums[j])
            
            if nums[i] in s:
                return True
            
            s.add(nums[i])
        
        return False

if __name__ == "__main__":
    yes = Solution()

    print(yes.containsNearbyDuplicate([1,0,1,1], 2))

