from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        dp = [0]*(max(nums)+ 1)
        for num in nums:
            dp[num] += 1

        count = 0
        for i in range(len(dp)-1):
            if dp[i] > 1:
                count += dp[i]-1
                dp[i+1] += (dp[i]-1)
        count += dp[-1]*(dp[-1]-1)//2
        return count

if __name__ == "__main__":
    yes = Solution()

    print(yes.minIncrementForUnique([3,2,1,2,1,7]))

