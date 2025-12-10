class Solution(object):
    def isMatch(self, s, p):
        
        start_s = 0
        start_p = 0
        
        while start_p < len(p) and start_s < len(s):
            
            while start_p < len(p) and start_s < len(s) and p[start_p] == s[start_s]:
                start_p += 1
                start_s += 1
            
            if start_p < len(p) and start_s < len(s):
            
                if p[start_p] == '.':
                    start_s += 1
                    start_p += 1
                    
                elif p[start_p] == '*':
                    constant = p[start_p - 1]
                    start_p += 1
                    if constant != '.':
                        ahead = -1
                        while start_p < len(p) and p[start_p]  == constant:
                            ahead += 1
                            start_p += 1
                            
                        while start_s < len(s) and s[start_s] == constant and ahead > 0:
                            ahead -= 1
                            start_s += 1
                        
                        if ahead > 0:
                            return False
                        else:
                            while start_p < len(p) and p[start_p]  == constant:
                                start_p += 1
                        
                        while start_s < len(s) and s[start_s] == constant:
                            start_s += 1
                    elif constant == '.':
                        if not(start_p < len(p)):
                            return True
                        
                        temp_start = start_p
                        conned = True    
                        while start_p < len(p) and start_s < len(s):
                            if conned:
                                while start_s < len(s) and p[start_p] != s[start_s]:
                                    start_s += 1
                                
                            conned = True
                                
                            while start_p < len(p) and start_s < len(s) and p[start_p] == s[start_s]:
                                start_p += 1
                                start_s += 1
                            
                            if start_p < len(p) and p[start_p] == '.':
                                start_p += 1
                                if start_p < len(p):
                                    if p[start_p] == '*':
                                        start_p += 1
                                        temp_start = start_p
                                        
                                        if start_p >= len(p):
                                            return True
                                    else:
                                        start_s += 1
                                else:
                                    start_s += 1
                                    
                            elif start_p + 1 < len(p):
                                start_p += 1
                                if p[start_p] != '*':
                                    start_p = temp_start
                                else:
                                    conned = False
                                    start_p += 1
                            elif start_s < len(s):
                                start_p = temp_start
                     
                else:
                    if start_p + 1 < len(p):
                        start_p += 1
                        if p[start_p] != '*':
                            return False
                        start_p += 1
                    else:
                        return False
                    
        if start_s != len(s):
            return False
        
        if start_p != len(p):
            while start_p < len(p):
                if p[start_p] != '*':
                    start_p += 1
                    if start_p < len(p):
                        if p[start_p] != '*':
                            return False
                        start_p += 1
                    else:
                        return False
            return True
        
        return True
            
            
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.isMatch("aaa", "ab*a*c*a"))