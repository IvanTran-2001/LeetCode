class Solution(object):
    def generateMatrix(self, n):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        start = [0,0]
        end = [n -1, n-1]
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        count = 1
        while True:
            
            if start[1] <= end[1]:
                for i in range(start[1],end[1] + 1):
                    matrix[start[0]][i] = count
                    count += 1
            else:
                break
            
            if start[0] < end[0]:
                for i in range(start[0] + 1, end[0] + 1):
                    matrix[i][end[1]] = count
                    count += 1
            else:
                break
            
            if start[0] < end[0] and start[1] < end[1]:
                for i in range(end[1] - 1, start[1] - 1, -1):
                    matrix[end[0]][i] = count
                    count += 1
            else:
                break
            
            if start[0] + 1 < end[0] and start[1] < end[1]:
                for i in range(end[0]-1, start[0], -1):
                    matrix[i][start[1]] = count
                    count += 1
            else:
                break
            
            start[0] += 1
            start[1] += 1
            
            end[0] -= 1
            end[1] -= 1
        
        return matrix
        
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.generateMatrix(3))

