class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = [0,0]
        minimal = len(s)
        
        for i in s:
            if i == 'a':
                count[0] += 1
            elif i == 'b':
                count[1] += 1
        
        start = 0
        end = len(s) - 1
        
        deletion = 0
        
        while start < end:
            
            b_count = 0
            a_count = 0

            while start < end and s[start] == 'a':
                count[0] -= 1
                start += 1
            
            while start < end and s[end] == 'b':
                count[1] -=1
                end -= 1
        
            while start < end:
                while start < end and s[start] == 'a':
                    count[0] -= 1
                    start += 1
                
                b_count = 0
                while start <= end and s[start] != 'a':
                    b_count += 1
                    start += 1
                
                diffCountB = 0
                temp = start
                while temp <= end and s[temp] != 'b':
                    temp += 1
                    diffCountB += 1
                
                if diffCountB >= b_count:
                    count[1] -= b_count
                    deletion += b_count
                    count[0] -= diffCountB
                    start = temp
                else:
                    break
            
            while start < end:
                    
                while start < end and s[end] == 'b':
                    count[1] -=1
                    end -= 1
            
                a_count = 0
                while start <= end and s[end] != 'b':
                    a_count += 1
                    end -= 1
                
                diffCountA = 0
                temp = end
                while temp <= end and s[temp] != 'a':
                    temp -= 1
                    diffCountA += 1
                
                if diffCountA >= a_count:
                    count[0] -= a_count
                    deletion += a_count
                    count[1] -= diffCountA
                    end = temp
                else:
                    break
            
            minimal = min(min(count) + deletion, minimal)
            
            if minimal < deletion:
                return minimal
            
            count[0] -= a_count
            count[1] -= b_count
            
            deletion += a_count + b_count

        if minimal < deletion:
            return minimal
        
        return deletion
            

            
                
                
        
        
if __name__ == "__main__":
    yes = Solution()

    print(yes.minimumDeletions("abbaababaaabbabaabbbaabbabbaaabbbaaaaabbbaaaaaaabababbaaaaaaabbabbbbababaaaabbabaaaabbbabbababbbbbbbbbbabaaababbaabbaaababaaba"))