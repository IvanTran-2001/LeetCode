class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        new_array = [1] * n
        
        self.pattern(new_array, m)
        
        return new_array[-1]
    
    def pattern(self, new_array, m):
        if m == 1:
            return 
        for i in range(1, len(new_array)):
            new_array[i] = new_array[i] + new_array[i-1]
            
        self.pattern(new_array, m - 1)


if __name__ == "__main__":
    yes = Solution()

    print(yes.uniquePaths(2,3))