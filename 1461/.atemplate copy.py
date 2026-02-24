class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        dict = {format(i, f"0{k}b"): 0 for i in range(2**k)}
        count = 0
        for i in range(len(s) - k + 1):
            substriing = s[i:i+k]
            if substriing in dict:
                if dict[substriing] == 0:
                    dict[substriing] = 1
                    count += 1
            
            if count == len(dict):
                return True
        
        return False



if __name__ == "__main__":
    yes = Solution()

    print(yes.hasAllCodes("00110110", 2))

