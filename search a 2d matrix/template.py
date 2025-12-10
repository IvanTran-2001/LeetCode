class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row_index = self.find_row(matrix, target)
        if row_index >= len(matrix):
            return False
        
        if self.binary_search(matrix[row_index], target) != -1:
            return True
        else:
            return False
    

    def find_row(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][-1] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return left
    
    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        
        
                        
        

if __name__ == "__main__":
    yes = Solution()

    print(yes.searchMatrix([[1],[3]], 3))