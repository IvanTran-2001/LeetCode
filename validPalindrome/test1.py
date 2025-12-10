class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) -1
        confirm = True
        while i < j:
            
            while not ((s[i].lower()) <= 'z' and (s[i].lower()) >= 'a'):
                i += 1
            
            while not ((s[j].lower()) <= 'z' and (s[j].lower()) >= 'a'):
                j-=1
            
            if (s[i].lower()) != (s[j].lower()):
                confirm = False
                
            
            j -= 1
            i += 1
        
        return confirm
            
            
        
        
        
if __name__ == "__main__":
    test = Solution()
    print(test.isPalindrome("A man, a plan, a canal: Panama"))
    