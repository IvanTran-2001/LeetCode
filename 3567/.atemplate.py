class Solution:
    def reverseSubmatrix(self, grid, x, y, k):

        pointer = x + k -1 


        while pointer > x:

            for i in range(k):
                grid[x][y + i], grid[pointer][y + i] = grid[pointer][y + i], grid[x][y + i]
            
            x += 1
            pointer -= 1
                

        return grid

if __name__ == "__main__":
    yes = Solution()

    print(yes.reverseSubmatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 1, 0, 3) == [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]] )
    print(yes.reverseSubmatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 1, 0, 3))

