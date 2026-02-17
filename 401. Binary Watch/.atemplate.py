class Solution:
    def readBinaryWatch(self, turnedOn: int):
        ans = list()
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    ans.append(f"{h}:{m:02d}")
        return ans
        
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.readBinaryWatch(2))
