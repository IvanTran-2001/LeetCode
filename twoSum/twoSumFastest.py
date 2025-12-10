class Solution(object):
    def twoSum(self, nums, target):
        prevMap={}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return (prevMap[diff],i)
            prevMap[n]=i
        return

if __name__ == "__main__":
    nums = [3,2,4]
    roman = Solution()
    print(roman.twoSum(nums, 6))
            