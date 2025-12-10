class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        max = len(s)
        if numRows == 1 or numRows >= max:
            return s
        
        first = (numRows-1)*2
        second = 0
        new_string = ""
        
        for i in range(numRows):
            count = 0
            bal = True
            while count + i < max:
                
                new_string += s[count + i]
                
                if bal:
                    if first != 0:
                        count += first
                    else:
                        count += second
                    bal = False
                else:
                    if second != 0:
                        count += second
                    else:
                        count += first
                    bal = True
            
            first -= 2
            second += 2
            
        
        return new_string
            
        
        
            
        
        
if __name__ == "__main__":
    test = Solution()
    print(test.convert("PAYPALISHIRING", 4))