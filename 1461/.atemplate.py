class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        val_dict = {}
        for i in range(len(s) - k + 1):
            val_dict[s[i:i+k]] = 0
        
        arr = [format(i, f"0{k}b") for i in range(2**k)]

        for i in arr:
            if i not in val_dict:
                return False
        
        return True



if __name__ == "__main__":
    yes = Solution()

    print(yes.hasAllCodes("00110", 2))

