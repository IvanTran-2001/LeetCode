class Solution(object):
    def isMatch(self, s, p):
        
        start = 0
        start1 = 0
        laststar = -1
        lastBack = 0
        
        while start < len(p):
            
            if start1 >= len(s):
                while start < len(p) and p[start] == '*':
                    start += 1
                
                if start == len(p):
                    return True
                
                return False
            
            if p[start] == s[start1]:
                start += 1
                start1 += 1
                
            elif p[start] == '?':
                start += 1 
                start1 += 1
                
            elif p[start] == '*':
                if start == len(p) - 1:
                    return True
                
                while start < len(p) and p[start] == '*':
                    start += 1
                
                laststar = start

                replace = 0
                while start < len(p) and p[start] == '?':
                    replace += 1
                    start += 1
                    while start < len(p) and p[start] == '*':
                        start += 1
                        
                
                replace_letter = 1
                while start + 1 < len(p) and p[start] == p[start + 1]:
                    start += 1
                    replace_letter += 1
                    
                
                if start < len(p):  
                    while start1 < len(s) and (s[start1] != p[start] or replace > 0):
                        replace -= 1
                        start1 += 1
                elif p[start - 1] == '*' or p[start - 1] == '?':
                    while start1 < len(s) and replace > 0:
                        replace -= 1
                        start1 += 1
                    if replace > 0:
                        return False
                    return True
                
                if replace > 0:
                    return False
                    
                if replace_letter > 1 and len(s) < start1 + replace_letter:
                    return False
                
                if replace_letter > 1:
                    while start1 < len(s):
                        
                        while start1 < len(s) and s[start1] != p[start]:
                            start1 += 1
                        
                        if len(s) < start1 + replace_letter:
                            return False
                            
                        stat = True
                        for i in range(0, replace_letter):
                            if p[start] == s[start1]:
                                start1 += 1
                            else:
                                stat = False
                                break
                        
                        if stat:
                            break
                        
                    
                    start += 1
                
                if start1 == len(s):
                    if start == len(p):
                        return True
                    if not(p[start] == '*' or p[start] == '?'):
                        return False

            else:
                if laststar >= 0:
                    start1 -= (start - laststar -1)
                    start = laststar
                    temp = start1
                    
                    if p[start] != '?':
                        
                        while start1 >= 0 and (s[start1] != p[start]):
                            start1 -= 1
                        
                        if lastBack == start1 or start1 < 0:
                            start1 = temp
                            while start1 < len(s) and (s[start1] != p[start]):
                                start1 += 1
                        
                        if start1 == len(s):
                            return False
                        
                        lastBack = start1
                    
                    
                else:
                    return False
        
        if start1 < len(s):
            if laststar >= 0:
                o = -1
                while p[o] != '*':
                    if p[o] != s[o] and p[o] != '?':
                        return False
                    o -= 1
                    
                return True
                
            return False
        
        if (not p and s) or (not s and p):
            return False
        
        return True
                    

if __name__ == "__main__":
    yes = Solution()

    print(yes.isMatch("baab", "*?ab*"))
    "aaaaaaabbaabbaab", "*aaaabbaa*a*"
    "abcabczzzde", "*abc???de*"
    "abefcdgiescdfimde", "ab*cd?i*de"
    "abcabcabczzzde", "*abc???de*"