class Solution(object):
    def threeSum(self, nums):
        result = []

        # Sort the array to make the solution unique
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        nums = sorted(count)
        
        if nums[0] > 0:
            return []

        for i in range(len(nums) - 2):

            left, right = i + 1, len(nums) - 1

            while left < right:
                
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

        return result

                    
        
        
                
if __name__ == "__main__":
    yes = Solution()
    print(yes.threeSum([-1,0,1,2,-1,-4]))
    