class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_dict = {}
        for i, n in enumerate(nums):
            try:
                name_value = my_dict[n]
                del my_dict[n]
            except KeyError:
                my_dict[n] = i
        
        key, value = next(iter(my_dict.items()))
        return key
            
if __name__ == "__main__":
    yes = Solution()
    print(yes.singleNumber([2, 2, 3, 3, 5]))