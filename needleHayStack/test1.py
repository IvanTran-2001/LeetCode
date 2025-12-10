class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length = len(needle)
        mLength = len(haystack)
        for i in range(mLength - length+1):
            if haystack[i:i+length] == needle:
                return i
        

        return -1
    
if __name__ == "__main__":
    yes = Solution()
    print(yes.strStr("mississippi", "issip"))
