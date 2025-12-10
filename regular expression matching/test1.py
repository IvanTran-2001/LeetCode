class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        alphabet = [0]*26
        All = False
        minus = len(p) - len(s)
        if minus < 0:
            return False
        
        for j in range(minus):
            for b in range(j):
                num = ord(p[b])-97 
                
                if (p[b] == '.'):
                    if not All:
                        All = True
                        for m, n in enumerate(alphabet):
                            alphabet[m] = 1
                elif (p[b] == '*'):
                    if alphabet[num] == 1:
                        alphabet[num] += 1
                        
                elif alphabet[num] == 0:
                    alphabet[num] += 1
                    
            for i, c in enumerate(s):
                num = ord(c)-97 
                if p[j+i] != c:
                    if (p[j+i] == '.'):
                        if not All:
                            All = True
                            for m, n in enumerate(alphabet):
                                alphabet[m] = 1
                    elif (p[j+i] == '*'):
                        if alphabet[num] == 1:
                            alphabet[num] += 1
                        else:
                            if minus == 0:
                                return False
                            else:
                                All = False
                                for m, n in enumerate(alphabet):
                                    alphabet[m] = 0
                                break
                    else:
                        if minus == 0:
                            return False
                        else:
                            All = False
                            for m, n in enumerate(alphabet):
                                alphabet[m] = 0
                            
                            break
                else:
                    if alphabet[num] == 0:
                        alphabet[num] += 1
                minus -= 1
        
        return True
        
                
            
                
            
if __name__ == "__main__":
    test = Solution()
    print(test.isMatch("ab", ".*c"))
    