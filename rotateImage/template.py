class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # self.print_matrix([[21,16,11,6,1],[22,17,12,7,2],[23,18,13,8,3],[24,19,14,9,4],[25,20,15,10,5]])
        boundary = 0
        while len(matrix) - boundary*2 > 1:
            
            # if boundary == 1:
            #     True
                
            start = 0 + boundary
            end = -1 - boundary
            for i in range(start, len(matrix) + end):
                matrix[start][i], matrix[i][end] =  matrix[i][end], matrix[start][i]
                
            matrix[start][start], matrix[end][end] = matrix[end][end], matrix[start][start]
            # self.print_matrix(matrix)
            
            for i in range(1 + boundary, len(matrix) + end):
                matrix[start][i], matrix[end][len(matrix) - i - 1] = matrix[end][len(matrix)- i - 1], matrix[start][i]
            
            matrix[start][start], matrix[end][start] = matrix[end][start], matrix[start][start]  
            # self.print_matrix(matrix)
            
            for i in range(1 + boundary, len(matrix) + end):
                matrix[start][i], matrix[- (i + 1)][start] =  matrix[- (i + 1)][start], matrix[start][i]
            # self.print_matrix(matrix)
            boundary += 1
        
    # def print_matrix(self, matrix):
    #     print()
    #     for i in matrix:
    #         print(i)

if __name__ == "__main__":
    yes = Solution()

    yes.rotate([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])