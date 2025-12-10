class NumArray:

    def __init__(self, nums):
        self.prefix_nums = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix_nums.append(self.prefix_nums[i - 1] + nums[i])
         

    def sumRange(self, left: int, right: int) -> int:
        if left -1 >= 0:
            return self.prefix_nums[right] - self.prefix_nums[left - 1]
        else:
            return self.prefix_nums[right]

if __name__ == "__main__":
    yes = NumArray([-2, 0, 3, -5, 2, -1])
    print(yes.sumRange(0, 2)); 
    print(yes.sumRange(2, 5)); 
    print(yes.sumRange(0, 5)); 

