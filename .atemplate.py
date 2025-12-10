class Solution(object):

    def climbStairs(self, n):
        sum = 1
        before = 1

        for i in range(n-1):
            after = sum
            sum += before
            before = after

        return sum

if __name__ == "__main__":
    yes = Solution()

    print(yes.climbStairs(3))

