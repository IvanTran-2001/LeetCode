import bisect
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        count = {}
        
        #Keep track of what numbers repeated and can be
        #used to find if a number exist within list with
        #O(n) run time speed
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        nums = sorted(count)
        
        result = []
        
        for i, num in enumerate(nums):
            
            #This is statement checks if the number is counted more than
            #once in the list
            if count[num] > 1:
                
                # the only possibility for x zeroes with 2 zeroes is 0
                # 0+0+x = 0 meaning x = 0.
                if num == 0:
                    if count[num] > 2:
                        result.append([0, 0, 0])
                else:
                    # if there r 2 numbers the same, there must be a doubled version
                    # but negative. EG -200 + -200 will need to get 400 for -200 + -200 + 400 = 0
                    if -2 * num in count:
                        result.append([num, num, -2 * num])
                        
            # This statement essentially gets the "selected" maximum and minimum number's index and loops in
            # between them. These maximum and minimums change dynamically depending on what the chosen number is
            # for the loop. Using the chosen number for this loop and the number chosen between the max and min
            # will determine the 3rd number if it exist or not.
            if num < 0:
                
                two_sum = -num
                
                # So bisect is a binary search that will either find the number
                # you are looking for or if the number doesn't exist, will find
                # what index should that number be inserted.
                
                # this bisect basically finds the minimum number's index that can
                # potentially work with the chosen number for this loop
                
                left = bisect.bisect_left(nums, (two_sum - nums[-1]), i + 1)
                
                # By doing two_sum//2, this line basically gives you the maximum number's
                # index required to find the 3rd number if it exists or not
                for i in nums[left:bisect.bisect_right(nums, (two_sum // 2), left)]:
                    
                    # The 3rd number that we try to find in list
                    j = two_sum - i
                    
                    # Checking if 3rd number exist
                    if j in count and j != i:
                        result.append([num, i, j])
                        
        return result

if __name__ == "__main__":
    yes = Solution()
    print(yes.threeSum([-300, 150, 150]))