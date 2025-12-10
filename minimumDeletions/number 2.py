class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_array = [None] * (len(s) + 1)
        new_array[0] = (None, -1)
        minimal = len(s)
        
        b4 = s[0]
        index = 0
        count = [0,0]
        end = 1
        
        for i in s:
            if b4 == i:
                index += 1
            else:
                new_array[end] = ((b4, index - 1))
                end += 1
                b4 = i
                index += 1
            
            if i == 'a':
                count[0] += 1
            elif i == 'b':
                count[1] += 1
        
        new_array[end] = (b4, len(s) - 1)

        start = 1
        
        deletion = 0
        
        while start < end:
            termB_1 = 0
            termA_1 = 0
            
            if start < end and new_array[start][0] == 'a':
                count[0] -= new_array[start][1] - new_array[start-1][1]
                start += 1
            
            if start < end and new_array[end][0] == 'b':
                count[1] -= new_array[end][1] - new_array[end - 1][1]
                end -= 1
            
            while start < end:
                termA_1 = 0
                termA_2 = 0
                if start <= end:
                    termA_1 = new_array[start][1] - new_array[start - 1][1]
                    termA_2 = new_array[start + 1][1] - new_array[start][1]
                    
                    start += 1
                    
                    if termA_1 > termA_2:
                        break
                    else:
                        deletion += termA_1
                        count[1] -= termA_1
                        count[0] -= termA_2
                        start += 1
            
            while start < end:
                termB_1 = 0
                termB_2 = 0
                if start <= end:
                    termB_1 = new_array[end][1] - new_array[end-1][1]
                    termB_2 = new_array[end-1][1] - new_array[end-2][1]
                    
                    end -= 1
                    
                    if termB_1 > termB_2:
                        break
                    else:
                        deletion += termB_1
                        count[0] -= termB_1
                        count[1] -= termB_2
                        end -= 1
            
            minimal = min(min(count) + deletion, minimal)
            
            if minimal <= deletion:
                return minimal
            
            count[1] -= termA_1
            count[0] -= termB_1
            
            deletion += termA_1 + termB_1
            
        if minimal <= deletion:
            return minimal
        
        return deletion
            
if __name__ == "__main__":
    yes = Solution()

    print(yes.minimumDeletions("aaababababbbaaabbbbabbb"))