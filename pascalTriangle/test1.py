class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if (numRows < 2):
            return [[1]]
        
        numList = [[1], [1,1]]        

        for i in range(2, numRows):
            tempList = [1]
            for j in range(i-1):
                tempList.append(numList[i-1][j]+ numList[i-1][j+1])

            tempList.append(1)
            numList.append(tempList)
                
        return numList

        
        
        
if __name__ == "__main__":
    test = Solution()
    for i in (test.generate(20)):
        print(i)