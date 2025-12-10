class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        
        row = 0
        half = (rowIndex + 1)//2 
        numList = [1, 1]
        
        while True:
            
            row += 1
            
            #Even Numbers
            for i in range(row, 0, -1): 
                numList[i] += numList[i-1]
            
            numList.append(numList[row-1])
            
            if numList[1] == rowIndex:
                for i in range(half-2, -1, -1):
                    numList.append(numList[i])
                return numList
            
            #Odd Numbers
            for i in range(row+1, 0, -1):
                numList[i] += numList[i-1]
                
            if numList[1] == rowIndex:
                for i in range(half - 2, -1, -1):
                    numList.append(numList[i])
                return numList
            
        
        
if __name__ == "__main__":
    test = Solution()
    print(test.getRow(13))