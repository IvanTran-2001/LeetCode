class Solution(object):

    def threeSum(self, nums):
        result = []

        # Sort the array to make the solution unique
        nums = sorted(nums)
        length = len(nums)
        
        if nums[0] > 0:
            return []

        for i in range(len(nums) - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1

            while left < length:
                
                if (nums[i] + nums[left]) * -1 > nums[length -1]:
                    break
                
                if left > i+1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                
                target = (nums[left] + nums[i]) * -1
                
                y = left + 1
                n = length - 1
                
                while y <= n:
                    mid = (y + n) // 2

                    if nums[mid] == target:
                        result.append([nums[i], nums[left], nums[mid]])
                        break
                    elif nums[mid] < target:
                        y = mid + 1  # Target is in the right half
                    else:
                        n = mid - 1  # Target is in the left half
                
                
                left += 1
                

        return result

                    
        
        
                
if __name__ == "__main__":
    yes = Solution()
    print(yes.threeSum([-1,0,1,2,-1,-4]))
    