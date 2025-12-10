class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()
        
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    if not(i in rows):
                        rows.add(i)
                    
                    if not(j in columns):
                        columns.add(j)
        
        for i in rows:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0
        
        for i in columns:
            for j in range(len(matrix)):
                matrix[j][i] = 0
        
        return matrix
                        
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))