class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
        max_len = len(s)
        first, second = (numRows - 1) * 2, 0
        rows = []
        
        for i in range(numRows):
            
            bal = True
            
            while i < max_len:
                
                rows.append(s[i])
                
                if bal:
                    i += first if first != 0 else second
                    bal = False
                else:
                    i += second if second != 0 else first
                    bal = True
            
            first -= 2
            second += 2
        
        return ''.join(rows)

if __name__ == "__main__":
    test = Solution()
    print(test.convert("PAYPALISHIRING", 4))