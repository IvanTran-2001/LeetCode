from collections import defaultdict
class Solution(object):
    def maximumLength(self, A, k):
        dp = [defaultdict(int) for i in range(k + 1)]
        res = [0] * (k + 1)
        for a in A:
            for i in range(k, -1, -1):
                dp[i][a] = max(dp[i][a] + 1, res[i - 1] + 1 if i else 0)
                res[i] = max(res[i], dp[i][a])
        return res[k]
            
if __name__ == "__main__":
    yes = Solution()

    print(yes.maximumLength([38,40,38,40], 1))

