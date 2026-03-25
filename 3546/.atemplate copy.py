from typing import List
class Solution:
    def canPartitionGrid(self, grid):
        prefix_x = []
        prefix_y = []

        total = 0
        for i, n in enumerate(grid):
            for j, m in enumerate(n):
                total += m
                if j == len(grid[0]) - 1:
                    prefix_x.append(total)

        total = 0
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                total += grid[j][i]
                if j == len(grid) - 1:
                    prefix_y.append(total)
        
        for i in range(len(prefix_y)):
            if prefix_y[i] == prefix_y[-1] - prefix_y[i]:
                return True
        
        for i in range(len(prefix_x)):
            if prefix_x[i] == prefix_x[-1] - prefix_x[i]:
                return True
        
        return False
                



if __name__ == "__main__":
    yes = Solution()

    print(yes.canPartitionGrid([[9753,4621,3652],[3003,4050,433]]))

