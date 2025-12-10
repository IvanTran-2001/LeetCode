class Solution(object):
    def minWindow(self, s, t):
        count_t = {}
        count_s = {}
        counter = 0
        
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        for c in s:
            if c in count_t:
                count_s[c] = count_s.get(c, 0) + 1
                
                if c in count_s:
                    if count_s[c] <= count_t[c]:
                        counter += 1
                else:
                    counter += 1
        
        if counter < len(t):
            return ""

        start = 0
        end = len(s) - 1
        
        while not(s[start] in count_t):
            start += 1
        
        while not(s[end] in count_t):
            end -= 1
        
        minimum_length = [start, end]
        
        while start <= end:
            
            temp_dict = {}
            temp = end
            while start <= temp:
                if not s[temp] in temp_dict:
                    temp_dict[s[temp]] = 0
                    
                if count_s[s[temp]] - (temp_dict[s[temp]] + 1) >= count_t[s[temp]]:
                    temp_dict[s[temp]] += 1
                    temp -= 1
                else:
                    if temp - start < minimum_length[1] - minimum_length[0]:
                        minimum_length = [start,temp]
                    
                    break
                
                while not(s[temp] in count_t):
                    temp -= 1
                
                if temp - start < minimum_length[1] - minimum_length[0]:
                    minimum_length = [start,temp]
                    
            if count_s[s[start]] - 1 >= count_t[s[start]]:
                count_s[s[start]] -= 1
                start += 1
            else:
                break
            
            while not(s[start] in count_t):
                start += 1
        
        return s[minimum_length[0]:minimum_length[1] + 1]
            
            
                
            
                

if __name__ == "__main__":
    yes = Solution()
    

    print(yes.minWindow("cabwefgewcwaefgcf", "cae"))

