class Solution:
    def minSumOfLengths(self, arr, target):
        ans = float('inf')
        prefix_sum = {0:-1}
        sum = 0
        for i, val in enumerate(arr):
            sum += val
            prefix_sum[sum] = i

        sum = 0

        minimum = float('inf')

        for i, val in enumerate(arr):
            sum += val

            if (sum - target) in prefix_sum:
                minimum = min(minimum, i - prefix_sum[sum - target])

            if ((sum + target) in prefix_sum):
                if (minimum < float('inf')):
                    ans = min(ans, minimum + prefix_sum[sum + target] - i)
        
        if ans == float('inf'):
            return -1
        
        return ans





if __name__ == "__main__":
    yes = Solution()
    arr = [3,2,2,4,3] 
    target = 3

    print(yes.minSumOfLengths(arr, target))

