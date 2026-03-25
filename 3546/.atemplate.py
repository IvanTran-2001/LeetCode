from typing import List
class Solution:
    def canPartitionGrid(self, grid):
        prefix_1 = []
        prefix_2 = []

        total = 0
        for i, n in enumerate(grid):
            prefix_1.append([])
            for j in n:
                total += j
                prefix_1[i].append(total)
        
        total = 0
        for i in range(len(grid[0])):
            prefix_2.append([])
            for j in range(len(grid)):
                total += grid[j][i]
                prefix_2[i].append(total)
        
        length = len(prefix_1) - 1
        length2 = len(prefix_2) - 1
        for i in range(len(prefix_1)):
            if prefix_1[i][-1] == prefix_1[length][-1] - prefix_1[i][-1]:
                return True
        
        for i in range(len(prefix_2)):
            if prefix_2[i][-1] == prefix_2[length2][-1] - prefix_2[i][-1]:
                return True
        
        return False
                



if __name__ == "__main__":
    yes = Solution()

    print(yes.canPartitionGrid([[28443],[33959]]))

