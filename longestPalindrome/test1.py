class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        length = len(s)
        index = 1

        while length != 0:

            for i in range(index):
                half = (length-1)//2+1
                y = s[i:half+i]
                x = s[i +length - half:i + length]
                if self.compare(y, x):
                    return s[i:i + length]
            
            index += 1
            length -= 1

        return "fuck you"
    
    def compare(self, y, x):
        for i, n in enumerate(y):
            if n != x[-i-1]:
                return False
        
        return True


            
        
        
if __name__ == "__main__":
    test = Solution()
    print(test.longestPalindrome("bacabab"))