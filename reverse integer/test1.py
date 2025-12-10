class Solution(object):
    def is_within_integer_range(self, num):
        return -2147483648 < num < 2147483647
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            num = int(str(x)[1::][::-1])
            num *= -1
        else:
            num = int(str(x)[::-1])
        if self.is_within_integer_range(num):
            return num
        else:
            return 0
            
        
        
        
        
if __name__ == "__main__":
    test = Solution()
    print(test.reverse(-45675))