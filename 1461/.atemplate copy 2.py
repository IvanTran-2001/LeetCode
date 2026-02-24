class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False

        need = 1 << k
        if n - k + 1 < need:
            return False

        seen = [False] * need
        mask = 0
        full = need - 1
        cnt = 0

        for i, ch in enumerate(s):
            mask = ((mask << 1) & full) | (ch == '1') # remove the leftmost and append the current bit
            if i < k - 1: continue
            if not seen[mask]:
                seen[mask] = True
                cnt += 1
                if cnt == need:
                    return True
        return False
    
if __name__ == "__main__":
    yes = Solution()

    print(yes.hasAllCodes("00110110", 2))

