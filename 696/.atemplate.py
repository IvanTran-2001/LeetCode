
class Solution():
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        l = 0
        r = 1

        while r < len(s):
            if s[r] == s[l]:
                if s[r - 1] != s[r]:
                    l += 1
                    while s[l] == s[l - 1] and l < r:
                        l += 1
                else:
                    r += 1
            else:
                l += 1
                ans += 1
                
                r += 1


        return ans
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.countBinarySubstrings("11110011"))

