from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        count = 0
        my_dict = {}
        start = [0,0]
        end = [len(grid) -1, len(grid[0])-1]
        
        if start[1] <= end[1]:
            for i in range(start[1], end[1] + 1):
                if grid[start[0]][i] == 1:
                    count -= search_ones(grid, start[0], i, my_dict)
                
        
        if start[0] < end[0]:
            for i in range(start[0] + 1, end[0] + 1):
                count -= search_ones(grid, i, end[1], my_dict)

        
        if start[0] < end[0] and start[1] < end[1]:
            for i in range(end[1] - 1, start[1] - 1, -1):
                count -= search_ones(grid, end[0], i, my_dict)

        
        if start[0] + 1 < end[0] and start[1] < end[1]:
            for i in range(end[0]-1, start[0], -1):
                count -= search_ones(grid, i, start[1], my_dict)
        

        return count + sum([sum(x) for x in grid])
    
def search_ones(matrix, x, y, my_dict):
    
    if not ((x, y) in my_dict) and x < len(matrix) and x >= 0 and y < len(matrix[0]) and  y >= 0:
        if matrix[x][y] != 1:
            return 0
        
        my_dict[(x, y)] = None
        
        count = 1
        count += search_ones(matrix, x + 1, y, my_dict)
        count += search_ones(matrix, x - 1, y, my_dict)
        count += search_ones(matrix, x, y + 1, my_dict)
        count += search_ones(matrix, x, y - 1, my_dict)
        
        return count
    else:
        return 0
    
    
    
    
    

if __name__ == "__main__":
    yes = Solution()
    grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    print(yes.numEnclaves(grid))

