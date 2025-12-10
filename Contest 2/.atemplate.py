from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        r_l = None
        r_h = None
        c_l = None
        c_h = None
        
        
        for i in range(len(grid)):
            for j in grid[i]:
                if j == 1:
                    r_l = i
                    break
                
            if r_l != None:
                break
        
        for i in range(len(grid)):
            for j in grid[-i - 1]:
                if j == 1:
                    r_h = -i + len(grid) - 1
                    break
            
            if r_h != None:
                break
        
        for i in range(len(grid[0])):
            for j in range(r_l, r_h + 1):
                if grid[j][i] == 1:
                    c_l = i
                    break
            if c_l != None:
                break
        
        for i in range(len(grid[0])):
            for j in range(r_l, r_h + 1):
                if grid[j][-i - 1] == 1:
                    c_h = len(grid[0]) - i - 1
                    break
            if c_h != None:
                break
        
        
        return (r_h - r_l + 1) * (c_h - c_l + 1)

if __name__ == "__main__":
    yes = Solution()
    print(yes.minimumArea([[0,1]]))