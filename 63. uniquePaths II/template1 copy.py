from functools import reduce
import operator

class Solution(object):
    def uniquePathsWithObstacles(self, matrix):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        max_location = [len(matrix), len(matrix[0])]
        if matrix[0][0] == 1 or matrix[max_location[0] - 1][max_location[1] - 1] == 1:
            return 0
        
        stars = []
        
        
        total = reduce(operator.mul, self.checker([0,0], max_location, [0,0]))
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 1:
                    stars.append(([[r,c],self.checker([r,c], max_location, [0,0])]))
        
        for i in range(len(stars)):
            for j in range(i + 1, len(stars)):
                
                if stars[i][0][0] <= stars[j][0][0] and stars[i][0][1] <= stars[j][0][1]:
                    stars[i][1][1] -= reduce(operator.mul, self.checker(stars[j][0], max_location, stars[i][0]))
            
            total -= stars[i][1][0] * stars[i][1][1]
        return total
                    
                
    def uniquePaths(self, m, n):
        if n == 0 or m == 0:
            return 1
        
        row = [1] * n

        for _ in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
    
    def checker(self, locate, max_locate, start_locate):
        
        x_left_side = self.uniquePaths(1 + locate[0] - start_locate[0], 1 + locate[1] - start_locate[1])
        
        x_right_side = self.uniquePaths(max_locate[0] - locate[0], max_locate[1] - locate[1])
        
        return [x_left_side, x_right_side]


if __name__ == "__main__":
    yes = Solution()
    matrix = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],[0,0],[1,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0]]
    print(yes.uniquePathsWithObstacles(matrix))