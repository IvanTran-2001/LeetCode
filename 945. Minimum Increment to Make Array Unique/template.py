from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        my_dict = {}
        moves = 0
        for i in nums:
            my_dict[i] = my_dict.get(i, 0) + 1
        
        nums = sorted(my_dict)
        number = 0
        for i in nums:
            if number < i:
                number = i
            if my_dict[i] > 1:
                for _ in range(my_dict[i] - 1):
                    moves += number - i
                    while number in my_dict:
                        number += 1
                        moves += 1
                    my_dict[number] = my_dict.get(number, 0) + 1
        
        return moves

if __name__ == "__main__":
    yes = Solution()

    print(yes.minIncrementForUnique([3,2,1,2,1,7]))

