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
        sign = 1
        
        while i < max_len and s[i] == " ":
            i += 1
            
        if i >= max_len:
            return 0
            
        if (s[i] == '-'):
            
            if (i+1 >= max_len) or not ('0' <= s[i+1] <= '9'):
                return 0
            sign = -1
            i += 1
            
        elif (s[i] == '+'):
            if (i+1 >= max_len) or not ('0' <= s[i+1] <= '9'):
                return 0
            
            i += 1
            
            
        num = ['0']
            
        while (i < max_len) and ('0' <= s[i] <= '9'):
            num.append(s[i])
            i += 1
        
        return self.is_within_integer_range(int(''.join(num)) * sign)
        
                    
if __name__ == "__main__":
    test = Solution()
    print(test.myAtoi("words and 987"))