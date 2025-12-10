import bisect
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 3:
            return sum(nums)
        
        minimum_sum = nums[0] + nums[1] + nums[2]
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        nums = sorted(count)
        
        if len(nums) == 1:
            return nums[0] * 3
        
        for i, num in enumerate(nums):
            

            if count[num] > 1:
                temp_target = (num * -2) + target
                temp_index = bisect.bisect_left(nums, temp_target)

                if temp_index >= len(nums):
                    temp_index -= 1
                
                minus_index = temp_index
                
                if temp_target < nums[temp_index]:
                    if temp_index - 1 >= 0:
                        minus_index -= 1
                    if abs(nums[minus_index] - temp_target) < abs(nums[temp_index] - temp_target):
                        temp_index = minus_index
                elif temp_target > nums[temp_index]:
                    if temp_index + 1 < len(nums):
                        minus_index += 1
                    if abs(nums[minus_index] - temp_target) < abs(nums[temp_index] - temp_target):
                        temp_index = minus_index
                else:
                    if temp_target == num:
                        if count[num] >= 3:
                            return target
                        else:
                            if abs(target - (nums[temp_index - 1] + 2*num)) < abs(target - (nums[temp_index + 1]+ 2*num)):
                                if temp_index - 1 < 0:
                                    temp_index += 1
                                else:
                                    temp_index -= 1
                            else:
                                if temp_index + 1 > len(nums):
                                    temp_index -= 1
                                else:
                                    temp_index += 1
                    else:
                        return target
                
                
                check_number = num * 2 + nums[temp_index]
                if abs(target - minimum_sum) > abs(target - check_number):
                    minimum_sum = check_number

            if len(nums) >= 3:
                
                two_sum = -num
                left_calc = (target - num - nums[-1] - abs(target - minimum_sum))
                right_calc = ((two_sum + target) // 2) + abs(target - minimum_sum)
                
                left = bisect.bisect_left(nums, left_calc, i + 1)
                right = bisect.bisect_right(nums, right_calc, left)
                
                for j in range(left, right):
                    
                    if nums[j] == num:
                        continue
                    
                    temp_target = -(num + nums[j]) + target
                    temp_index = bisect.bisect_left(nums, temp_target)

                    if temp_index >= len(nums):
                        temp_index -= 1
                    
                    minus_index = temp_index
                    
                    if temp_target < nums[temp_index]:
                        if temp_index - 1 >= 0:
                            minus_index -= 1
                        if abs(nums[minus_index] - temp_target) < abs(nums[temp_index] - temp_target):
                            temp_index = minus_index
                    elif temp_target > nums[temp_index]:
                        if temp_index + 1 < len(nums):
                            minus_index += 1
                        if abs(nums[minus_index] - temp_target) < abs(nums[temp_index] - temp_target):
                            temp_index = minus_index
                    else:
                        if num != nums[temp_index] and nums[j] != nums[temp_index]:
                            return target
                        else:       
                            if temp_index - 1 >= 0 and temp_index + 1 < len(nums):
                                if abs(target - (nums[temp_index - 1] + num + i)) < abs(target - (nums[temp_index + 1]+ num + i)):
                                    temp_index -= 1
                                else:
                                    temp_index += 1
                            else:
                                if temp_index - 1 > 0:
                                    temp_index -= 1
                                elif temp_index + 1 < len(nums):
                                    temp_index += 1

                    if num != nums[temp_index] and nums[j] != nums[temp_index]:
                        check_number = num + nums[j] + nums[temp_index]
                        if abs(target - minimum_sum) > abs(target - check_number):
                            minimum_sum = check_number
                    
                        
        return minimum_sum

if __name__ == "__main__":
    yes = Solution()
    print(yes.threeSumClosest())