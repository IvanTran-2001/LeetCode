class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s:
            return 0
        now, flag = 0, s[0]
        prev = 0
        res = 0
        for x in s:
            if x==flag:
                now += 1
            else:
                res += min(now, prev)
                prev = now
                now, flag = 1, x
        res += min(now, prev)
        return res
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.countBinarySubstrings("11110011"))

