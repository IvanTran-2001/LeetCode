class Solution(object):
    def is_within_integer_range(self, num):
        if -2147483648 > num:
            return -2147483648
        elif num > 2147483647:
            return 2147483647
        else:
            return num
        
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = len(s)
        i = 0
        
        while i < max_len and s[i] == " ":
            i += 1
            
        
        while i < max_len:
            
            if '0' <= s[i] <= '9':
                
                num = []
                sign = 1
                if i > 0 and s[i-1] == '-':
                    sign = -1
                    
                while (i < max_len) and ('0' <= s[i] <= '9'):
                    num.append(s[i])
                    i += 1
                
                return self.is_within_integer_range(int(''.join(num)) * sign)
            
            elif (s[i] == '-') or (s[i] == '+'):
                if i+1 >= max_len or not ('0' <= s[i+1] <= '9'):
                    return 0
            else:
                return 0
            
            i += 1
        
        return 0