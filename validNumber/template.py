class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        DECIMAL = 0
        NUMBER = 1
        LETTER_E = 2
        
        #Sign, Decimal, Number, E
        checkList = [False, False, False]
        
        start = 0
        if ord(s[0]) == 43 or ord(s[0]) == 45:
            if 1 == len(s):
                return False
            
            start += 1
            
        
        for i in range(start, len(s)):
            c = ord(s[i])
            
            if c == 43 or c == 45:
                if not(ord(s[i - 1]) == 101 or ord(s[i - 1]) == 69):
                    return False
                if (i + 1 == len(s)):
                    return False
                if not ((ord(s[i + 1]) >= 48 and ord(s[i + 1])) <= 57 or ord(s[i + 1]) == 43 or ord(s[i + 1]) ==45):
                    return False
            elif c >= 48 and c <= 57:
                checkList[NUMBER] = True
                
            elif c == 101 or c == 69:
                if checkList[LETTER_E] or (not checkList[NUMBER]) :
                    return False
                if (i + 1 == len(s)):
                    return False
                if not ((ord(s[i + 1]) >= 48 and ord(s[i + 1])) <= 57 or ord(s[i + 1]) == 43 or ord(s[i + 1]) == 45):
                    return False
                
                checkList[LETTER_E] = True
                
            elif c == 46:
                if checkList[DECIMAL]:
                    return False 
                
                if checkList[LETTER_E]:
                    return False
                
                checkList[DECIMAL] = True
            else:
                return False
        
        if checkList[DECIMAL] and not checkList[NUMBER]:
            return False
                    
        return True

if __name__ == "__main__":
    yes = Solution()

    print(yes.isNumber(".e1"))