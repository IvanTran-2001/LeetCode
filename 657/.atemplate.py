class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ans = [0, 0]

        for i in moves:
            if i == "L":
                ans[0] -= 1
            elif i == "R":
                ans[0] += 1
            elif i == "U":
                ans[1] += 1
            else:
                ans[1] -= 1

        return ans[0] == 0 and ans[1] == 0

if __name__ == "__main__":
    yes = Solution()

    print(yes.judgeCircle([], 2))
