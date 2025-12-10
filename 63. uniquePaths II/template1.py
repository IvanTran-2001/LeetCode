class Solution(object):
    def uniquePathsWithObstacles(self, locateX, matrix):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # locateX = [-1,-1]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 1:
        #             locateX = [i, j]
        #             break
            
        #     if locateX[0] != -1:
        #         break
        
        if locateX[0] == -1:
            xLocationArray = [1] * (len(matrix))
            return self.pattern(xLocationArray, len(matrix[0]))
        
        xLocationArray = [1] * (locateX[0] + 1)
        num = locateX[1] + 1
        x_left_side = self.pattern(xLocationArray, num)
        
        num = len(matrix[0]) - locateX[1]
        xLocationArray = [1] * (len(matrix) - locateX[0])
        x_right_side = self.pattern(xLocationArray, num)
        
        xLocationArray = [1] * (len(matrix))
        total = self.pattern(xLocationArray, len(matrix[0]))
        
        return (x_right_side * x_left_side)
        
        
    
    def pattern(self, new_array, m):
        if m == 1:
            return new_array[-1]
        for i in range(1, len(new_array)):
            new_array[i] = new_array[i] + new_array[i-1]
            
        return self.pattern(new_array, m - 1)


if __name__ == "__main__":
    yes = Solution()
    matrix = [[0 for _ in range(42)] for _ in range(2)]
    
    print(yes.uniquePathsWithObstacles([0,6], matrix))