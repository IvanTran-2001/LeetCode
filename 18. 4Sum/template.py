import bisect
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        count = {}
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        nums = sorted(count)
        
        result = []
        
        start = 0
        
        for first_num in nums:
            
            adjusted_target = target - first_num
            count[first_num] -= 1
            
            if count[first_num] <= 0:
                start += 1
            
            for i in range(start, len(nums)):
                num = nums[i]
                
                if count[num] > 1:
                    if adjusted_target - (2 * num) == num:
                        if num == first_num:
                            if count[num] >= 3:
                                count[num] = 3
                                result.append([num,num,num,num])
                        else:
                            if count[num] >= 3:
                                result.append([first_num,num,num,num])
                    else:            
                        if adjusted_target - (2 * num) in count and count[adjusted_target - (2 * num)] > 0:
                            result.append([first_num, num, num, adjusted_target - (2 * num)])

                    
                two_sum = -num
                
                left = bisect.bisect_left(nums, (two_sum - nums[-1]) - abs(adjusted_target), i + 1)
                right = bisect.bisect_right(nums, ((two_sum + adjusted_target) // 2), left)

                
                for k in range(left,right):
                    k_num = nums[k]
                    j = two_sum - k_num + adjusted_target
                    
                    if j in count and j != k_num and j != first_num and count[j] > 0:
                        result.append([first_num, num, k_num, j])
            
            if count[first_num] > 0:
                start += 1
            
            count[first_num] = 0
        return result

if __name__ == "__main__":
    yes = Solution()
    print(yes.fourSum([-1,0,1,2,-1,-4], -1))