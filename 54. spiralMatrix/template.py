class Solution(object):
    def __init__(self):
        self.new_array = []
        
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.recurse(matrix, 0, 0, len(matrix)//2)
        return self.new_array
    
    def recurse(self, matrix, length, row, maxlength):
        
        # new_array = self.new_array
        
        if not(length + 1 > maxlength) or (len(matrix) % 2 == 1):
            for i in range(row, len(matrix[0]) - row):
                self.new_array.append(matrix[row][i])
        
        if length + 1 > maxlength:
            return
        
        for i in range(row + 1, len(matrix) - row):
            self.new_array.append(matrix[i][-1 - row])
            
        for i in range(len(matrix[0]) - row - 2, -1 + row, -1):
            self.new_array.append(matrix[-1 - row][i])
        
        if len(matrix[0]) - row > 2:
            for i in range(len(matrix) - row - 2, row, -1):
                self.new_array.append(matrix[i][0 + row])
            
        self.recurse(matrix, length + 1, row + 1, maxlength)
            
        
        
        
        

if __name__ == "__main__":
    yes = Solution()
    # a = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
    a = [[1,2,3],[4,5,6],[7,8,9]]
    for i in a:
        print(i)
        
    print(yes.spiralOrder(a))
