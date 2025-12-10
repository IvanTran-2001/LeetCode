class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        new_array = [[]]
        my_dict = {}
        
        for i in range(len(nums)):
            if nums[i] in my_dict and my_dict[nums[i]][0] == 1:
                continue
            else:
                my_dict[nums[i]] = [1,0]
                new_array.append([nums[i]])
                for j in range(i + 1, len(nums)):
                    
                    if nums[j] in my_dict:
                        if my_dict[nums[j]][1] == i + 2:
                            continue
                        else:
                            my_dict[nums[j]][1] = i + 2
                    else:
                        my_dict[nums[j]] = [0, i + 2]
                        
                    for k in range(j + 1, len(nums) + 1):
                        
                        new_array.append([nums[i]] + nums[j:k])
            
        return new_array

if __name__ == "__main__":
    yes = Solution()

    print(yes.subsetsWithDup([1,2,2,3]))

