class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        start = [0,0]
        end = [len(matrix) -1, len(matrix[0])-1]
        while True:
            
            if start[1] <= end[1]:
                result += matrix[start[0]][start[1]:end[1] + 1]
            else:
                break
            
            if start[0] < end[0]:
                for i in range(start[0] + 1, end[0] + 1):
                    result.append(matrix[i][end[1]])
            else:
                break
            
            if start[0] < end[0] and start[1] < end[1]:
                for i in range(end[1] - 1, start[1] - 1, -1):
                    result.append(matrix[end[0]][i])
            else:
                break
            
            if start[0] + 1 < end[0] and start[1] < end[1]:
                for i in range(end[0]-1, start[0], -1):
                    result.append(matrix[i][start[1]])
            else:
                break
            
            start[0] += 1
            start[1] += 1
            
            end[0] -= 1
            end[1] -= 1
        
        return result
        

if __name__ == "__main__":
    yes = Solution()
    matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
    print(yes.spiralOrder(matrix))

