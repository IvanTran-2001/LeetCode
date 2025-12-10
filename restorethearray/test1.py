class Solution(object):
    def numberOfArrays(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        length = len(s)

        for i in range(length + 1):
            self.sppp(i, s)
            
    def sppp(self, iD, s):
        arrOutput = []
        for i in range(iD*len(s)):
             
        return arrOutput


if __name__ == "__main__":
    yes = Solution()
    print(yes.numberOfArrays("1234567890", 90))