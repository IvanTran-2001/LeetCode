class Solution(object):
    def isMatch(self, s, p):
        
        if len(p) == 1 and len(s) > 1:
            return False
        
        new_array = [[0] * len(s) for _ in range(len(p))]
        
        start_s = 0
        start_p = 0
        
        if start_p + 1 < len(p) and p[start_p + 1] == '*':
            if p[start_p] == '.':
                for i in range(len(s)):
                    new_array[start_p + 1][i] = 3
            else:
                if s[start_s] != p[start_p] and start_p < len(p) - 2:
                    new_array[start_p + 1][0] = 2
                else:
                    for i, n in enumerate(s):
                        if n == p[start_p]:
                            new_array[start_p + 1][i] = 3

                            if i + 1 < len(s) and start_p < len(p) - 2:
                                new_array[start_p + 1][i+1] = 2
                        else:
                            break
            
            start_p = 2
                    
        else:
            if p[start_p] == s[start_s] or p[start_p] == '.':
                new_array[start_p][0] = 1
                
                if 1 < len(s):
                    new_array[start_p][1] = 2
                    
                start_p = 1
                start_s = 1
            else:
                return False
        
        while start_p < len(p) and start_s < len(s):
            
            if start_p + 1 < len(p) and p[start_p + 1] == '*':
                if p[start_p] == '.':
                    for i in range(start_s, len(s)):
                        new_array[start_p + 1][i] = 3
                else:
                    for i in range(start_s, len(s)):
                        if s[i] == p[start_p]:
                            if (new_array[start_p - 1][i] > 1) or ((new_array[start_p + 1][i - 1] == 3) and (s[i - 1] == p[start_p])):
                                new_array[start_p + 1][i] = 3
                                if i + 1 < len(s) and start_p < len(p) - 2:
                                    new_array[start_p + 1][i + 1] = 2
                                    
                            elif (new_array[start_p - 1][i] == 1):
                                if new_array[start_p + 1][i] == 2:
                                     new_array[start_p + 1][i] = 3
                                else:
                                    new_array[start_p + 1][i] = 1
                                
                                    
                        elif (new_array[start_p - 1][i] > 0):
                            if new_array[start_p - 1][i] == 1 and new_array[start_p + 1][i] == 2:
                                new_array[start_p + 1][i] = 3
                            else:
                                new_array[start_p + 1][i] = new_array[start_p - 1][i]
                start_p += 2
            else:                
                count = False
                if p[start_p] == '.':
                    for i in range(start_s, len(s)):
                        if new_array[start_p - 1][i] > 1:
                            count = True
                            if (new_array[start_p][i] == 2):
                                new_array[start_p][i] = 3
                            else:
                                new_array[start_p][i] = 1
                                
                            if i + 1 < len(s) and start_p < len(p) - 1:
                                new_array[start_p][i + 1] = 2
                            
                    
                    start_s += 1
                else:
                    for i in range(start_s, len(s)):
                        if (new_array[start_p - 1][i] > 1) and s[i] == p[start_p]:
                            if not count:
                                start_s = i + 1
                                count = True
                            
                            if new_array[start_p][i] == 2:
                                new_array[start_p][i] = 3
                            else:
                                new_array[start_p][i] = 1
                                
                            if i + 1 < len(s) and start_p < len(p) - 1:
                                new_array[start_p][i + 1] = 2
                
                if not count:
                    break

                start_p += 1
                
        if start_p < len(p):
            if (len(p) - start_p) % 2 != 0:
                return False
            
            for i in range(start_p + 1, len(p), 2):
                if p[i] != '*':
                    return False
            
            return True
        
        if new_array[len(p)-1][len(s)-1] == 1 or new_array[len(p)-1][len(s)-1] == 3:
            return True
        
        return False
        
        
        
        
            
if __name__ == "__main__":
    yes = Solution()
    val1, val2 = "abbbaabccbaabacab", "ab*b*b*bc*ac*.*bb*"
    yup = yes.isMatch(val1, val2)
    if isinstance(yup, list):
        for i, n in enumerate(yup):
            print(n, i)
    else:
        print(yup)